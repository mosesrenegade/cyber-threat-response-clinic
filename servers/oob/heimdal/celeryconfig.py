from celery.schedules import crontab
import os

try:
    if os.environ.get['FLASK_ENV']=='development':
        f=open("/heimdal/sess_id.txt","r")
    else:
        f=open("/heimdal/data/sess_id.txt","r")
    session_id=f.readlines()
except:
    pass

CELERY_IMPORTS = ['app', 'tasks']
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'heartbeat': {
        'task': 'put_to_api',
        'schedule': crontab(minute="*"),
        'args': session_id,
    }
}
