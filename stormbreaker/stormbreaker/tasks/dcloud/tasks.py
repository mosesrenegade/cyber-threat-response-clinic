"""dCloud Task Code."""

import logging
from datetime import datetime, timedelta

from stormbreaker.celery import app
from stormbreaker.config import DCLOUD_SESSION_EXPIRATION_TIME
from stormbreaker.mongo import db
from stormbreaker.tasks.cloud_accounts.tasks import clean_cloud_account


logger = logging.getLogger(__name__)


@app.task()
def cleanup_dcloud_session(session_id):
    logger.info("Beginning cleanup of dCloud session `{}`".format(session_id))

    # Get session details
    session_details = db.dcloud_sessions.find_one({"sessionId": session_id})
    if not session_details:
        logger.critical(
            "Unable to retrieve details for dCloud session`{}` from the "
            "MongoDB database".format(session_id)
        )
        return

    cloud_account = session_details.get("cloudAccount")
    cloud_login = cloud_account.get("login") if cloud_account else None

    if cloud_login:
        logger.info(
            "Scheduling the cleaning of cloud login `{}`".format(cloud_login)
        )
        clean_cloud_account.delay(cloud_login)
    else:
        logger.warning(
            "No cloud account assigned to dCloud session `{}`"
            "".format(session_id)
        )

    # Delete the dCloud session
    logger.info("Removing dCloud session `{}`".format(session_id))
    db.dcloud_sessions.delete_one({"sessionId": session_id})


@app.task()
def check_for_expired_dcloud_sessions():
    logger.info("Checking for expired dCloud sessions")
    expiration_time = datetime.utcnow() \
                      - timedelta(minutes=DCLOUD_SESSION_EXPIRATION_TIME)

    expired_sessions = list(db.dcloud_sessions.find({
        "lastCheckIn": {"$lt": expiration_time},
    }))

    logger.info(
        "Found {} expired dcloud sessions".format(len(expired_sessions))
    )

    for session in expired_sessions:
        logger.info(
            "Scheduling cleanup of session `{}`".format(session["sessionId"])
        )
        cleanup_dcloud_session.delay(session["sessionId"])
