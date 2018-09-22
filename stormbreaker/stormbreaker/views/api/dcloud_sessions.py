"""dCloud Sessions API endpoints."""

from datetime import datetime

import pymongo
from flask import jsonify, request, Response

from stormbreaker import app
from stormbreaker.mongo import db


@app.route('/api/dcloud/sessions', methods=['GET'])
def list_dcloud_sessions():
    sessions = list(db.dcloud_sessions.find({}, {'_id': False}))
    return jsonify(sessions)


@app.route('/api/dcloud/sessions/<session_id>', methods=['GET'])
def get_dcloud_session_details(session_id):
    session_details = db.dcloud_sessions.find_one(
        {"sessionId": session_id},
        projection={'_id': False},
    )
    return jsonify(session_details)


@app.route('/api/dcloud/sessions/<session_id>', methods=['PUT'])
def dcloud_session_update(session_id):
    try:
        data = request.json or {}
    except TypeError:
        return Response(
            "We encountered an error while parsing the JSON request body.",
            status=400,
        )

    if not isinstance(data, dict):
        return Response(
            "Incorrect top-level JSON data type. The request body should "
            "contain a JSON object.",
            status=400,
        )

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

    return jsonify(session_details)
