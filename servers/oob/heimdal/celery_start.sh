#!/bin/bash

cd heimdal

celery -A app.celery worker --loglevel=INFO &
celery beat -A app.celery --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid &
