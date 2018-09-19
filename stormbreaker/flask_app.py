#!/usr/bin/env python3
"""Stormbreaker APIs."""

import os
from datetime import datetime

import pymongo
from flask import Flask, Response, jsonify, request


MONGO_URL = os.environ.get("MONGO_URL")


mongo = pymongo.MongoClient(MONGO_URL)
db = mongo["flask_app"]


app = Flask(__name__)


@app.route('/api/cloudAccounts', methods=['POST'])
def post_cloud_accounts():
    try:
        data = request.json
        assert isinstance(data, list)
        assert len(data) > 0
        assert all([
            isinstance(record, dict) and record.get("login")
            for record in data
        ])

        if "cloud_accounts" in db.collection_names():
            db.cloud_accounts.drop()

        db.cloud_accounts.create_index(
            [("login", pymongo.ASCENDING)],
            unique=True,
        )
        db.cloud_accounts.insert_many(data)

    except TypeError as error:
        return Response(str(error), status=400)

    except AssertionError as error:
        return Response(str(error), status=400)

    else:
        return Response(status=201)


@app.route('/api/cloudAccounts', methods=['GET'])
def list_cloud_accounts():
    data = list(db.cloud_accounts.find({}, {'_id': False}))
    return jsonify(data)


@app.route('/api/cloudAccounts/assign', methods=['POST'])
def assign_cloud_account():
    try:
        session_id = request.args.get('sessionId')
        assert session_id is not None

        available_accounts = list(db.cloud_accounts.find(
            {"status": "available"},
        ))

        if not available_accounts:
            return Response("No cloud accounts available.", status=500)

        available_account = available_accounts[0]

        cloud_account = db.cloud_accounts.find_one_and_update(
            {"_id": available_account["_id"]},
            {
                "$set": {"status": "assigned"}
            },
            projection={'_id': False},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        if "dcloud_sessions" not in db.collection_names():
            db.dcloud_sessions.create_index(
                [("sessionId", pymongo.ASCENDING)],
                unique=True
            )

        db.dcloud_sessions.insert({
            "sessionId": session_id,
            "lastCheckIn": datetime.utcnow(),
            "cloudAccount": cloud_account,
        })

    except AssertionError as error:
        return Response(str(error), status=400)

    else:
        return jsonify(cloud_account)


@app.route('/api/dcloud/sessions', methods=['GET'])
def list_dcloud_sessions():
    data = list(db.dcloud_sessions.find({}, {'_id': False}))
    return jsonify(data)


@app.route('/api/dcloud/sessions/<session_id>', methods=['PUT'])
def dcloud_session_update(session_id):
    try:
        data = request.json or {}
        assert isinstance(data, dict)

        data.update(
            sessionId=session_id,
            lastCheckIn=datetime.utcnow(),
        )

        session_details = db.dcloud_sessions.find_one_and_update(
            {"sessionId": session_id},
            {"$set": data},
            projection={'_id': False},
            return_document=pymongo.ReturnDocument.AFTER,
        )

    except TypeError as error:
        return Response(str(error), status=400)

    except AssertionError as error:
        return Response(str(error), status=400)

    else:
        return jsonify(session_details)


if __name__ == '__main__':
    app.run()
