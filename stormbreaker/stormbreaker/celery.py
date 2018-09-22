"""Stormbreaker Celery App."""

from __future__ import absolute_import, unicode_literals

from celery import Celery


app = Celery("stormbreaker")
app.config_from_object("celeryconfig")
app.autodiscover_tasks([
    "stormbreaker.tasks.cloud_accounts",
    "stormbreaker.tasks.dcloud",
])
