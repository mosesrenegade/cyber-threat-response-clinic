"""Centralize package default and environment configuration."""

import os


# Configurations sourced from the environment
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")

# dCloud session expiration time (in minutes)
DCLOUD_SESSION_EXPIRATION_TIME = int(os.environ.get(
    "DCLOUD_SESSION_EXPIRATION_TIME", 15
))

SELENIUM_COMMAND_EXECUTOR_URL = os.environ.get(
    "SELENIUM_COMMAND_EXECUTOR_URL", "http://localhost:4444/wd/hub"
)


# Static App Configurations
CISCO_AMP_CONSOLE_URL = "https://console.amp.cisco.com"
