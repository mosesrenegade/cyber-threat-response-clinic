#!/usr/bin/env python
"""Stormbreaker Celery Configuration."""

import os
import urllib.parse
from urllib.parse import urljoin


# Configure the urllib parser to add support for `redis` schemes
urllib.parse.uses_relative.append('redis')
urllib.parse.uses_netloc.append('redis')


REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
REDIS_CELERY_BROKER_DATABASE = os.environ.get(
    "REDIS_CELERY_BROKER_DATABASE",
    default="1"
)
REDIS_CELERY_RESULTS_DATABASE = os.environ.get(
    "REDIS_CELERY_RESULTS_DATABASE",
    default="2",
)


broker_url = urljoin(REDIS_URL, REDIS_CELERY_BROKER_DATABASE)

result_backend = urljoin(REDIS_URL, REDIS_CELERY_RESULTS_DATABASE)
result_expires = 86400

imports = ('stormbreaker.tasks',)


# Scheduled Tasks
beat_schedule = {
    'scheduler_heartbeat': {
        'task': 'stormbreaker.tasks.scheduler_heartbeat',
        'schedule': 10.0,
    },
}
