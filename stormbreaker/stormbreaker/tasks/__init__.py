"""Celery Tasks."""

import logging

from stormbreaker.celery import app


logger = logging.getLogger(__name__)


@app.task()
def scheduler_heartbeat():
    logger.info("Celery Scheduler is Running")
