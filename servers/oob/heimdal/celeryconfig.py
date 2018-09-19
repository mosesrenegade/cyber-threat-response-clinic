from celery.schedules import crontab
import os
import redis

session_id =''

try:
    #if os.environ.get['FLASK_ENV']=='development':
    #    REDIS_HOST='localhost'

    #else:
        
    r = redis.StrictRedis(host='REDIS_HOST', port=6379, db=0)
    session_id=r.get('session_id')

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
