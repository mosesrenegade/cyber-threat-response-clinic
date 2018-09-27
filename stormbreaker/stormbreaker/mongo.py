"""MongoDB database access."""

import pymongo

from stormbreaker.config import MONGO_URL


client = pymongo.MongoClient(MONGO_URL)
db = client["stormbreaker"]


def init_cloud_accounts_collection():
    """Initialize the Stormbreaker cloud_accounts collection."""
    db.cloud_accounts.create_index(
        [("login", pymongo.ASCENDING)],
        unique=True,
    )


def init_dcloud_sessions_collection():
    db.dcloud_sessions.create_index(
        [("sessionId", pymongo.ASCENDING)],
        unique=True
    )


# Initialize collections at module load
if "cloud_accounts" not in db.collection_names():
    init_cloud_accounts_collection()

if "dcloud_sessions" not in db.collection_names():
    init_dcloud_sessions_collection()
