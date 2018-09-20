"""Cloud Accounts API endpoints."""

from datetime import datetime

import pymongo
from flask import Response, jsonify, request

from stormbreaker import app
from stormbreaker.mongo import db, init_cloud_accounts_collection


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

    except TypeError as error:
        return Response(str(error), status=400)

    except AssertionError as error:
        return Response(str(error), status=400)

    if "cloud_accounts" in db.collection_names():
        db.cloud_accounts.drop()
        init_cloud_accounts_collection()

    db.cloud_accounts.insert_many(data)

    return Response(status=201)


@app.route('/api/cloudAccounts', methods=['GET'])
def list_cloud_accounts():
    data = list(db.cloud_accounts.find({}, {'_id': False}))
    return jsonify(data)


@app.route('/api/cloudAccounts/assign', methods=['POST'])
def assign_cloud_account():
    session_id = request.args.get('sessionId')
    if not session_id:
        return Response(
            "The request was missing the required `sessionId` parameter.",
            status=400
        )

    # Check for an existing assignment
    dcloud_session = db.dcloud_sessions.find_one(
        {"sessionId": session_id},
        projection={'_id': False},
    )
    if dcloud_session:
        return jsonify(dcloud_session["cloudAccount"])

    # Assign a cloud account
    cloud_account = db.cloud_accounts.find_one_and_update(
        {"status": "available"},
        {"$set": {"status": "assigned"}},
        projection={'_id': False},
        return_document=pymongo.ReturnDocument.AFTER,
    )

    if cloud_account is None:
        return Response("No cloud accounts available.", status=500)

    db.dcloud_sessions.insert({
        "sessionId": session_id,
        "lastCheckIn": datetime.utcnow(),
        "cloudAccount": cloud_account,
    })

    return jsonify(cloud_account)
