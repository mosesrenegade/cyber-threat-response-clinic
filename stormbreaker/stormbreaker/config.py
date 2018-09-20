"""Centralize package default and environment configuration."""

import os


MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
