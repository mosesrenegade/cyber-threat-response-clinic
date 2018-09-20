"""Cloud Accounts API endpoints."""

from datetime import datetime

import pymongo
from flask import Response, jsonify, request

from stormbreaker import app
from stormbreaker.mongo import db, init_cloud_accounts_collection


@app.route('/api/cloud/accounts', methods=['POST'])
def post_cloud_accounts():
    try:
        data = request.json
    except TypeError:
        return Response(
            "We encountered an error while parsing the JSON request body.",
            status=400,
        )

    if not isinstance(data, list) or \
        not len(data) > 0 or \
        not all([
            isinstance(record, dict) and record.get("login")
            for record in data
        ]):

        return Response(
            "The JSON data in the request body was not the expected format.",
            status=400,
        )

    if "cloud_accounts" in db.collection_names():
        db.cloud_accounts.drop()
        init_cloud_accounts_collection()

    db.cloud_accounts.insert_many(data)

    return Response(status=201)


@app.route('/api/cloud/accounts', methods=['GET'])
def list_cloud_accounts():
    data = list(db.cloud_accounts.find({}, {'_id': False}))
    return jsonify(data)


@app.route('/api/cloud/accounts/<login>', methods=['GET'])
def get_cloud_account_details(login):
    account_details = db.cloud_accounts.find_one(
        {"login": login},
        projection={'_id': False},
    )

    if not account_details:
        return Response(
            "We could not locate the cloud account for the login provided.",
            status=404,
        )

    return jsonify(account_details)


@app.route('/api/cloud/accounts/assign', methods=['POST'])
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
