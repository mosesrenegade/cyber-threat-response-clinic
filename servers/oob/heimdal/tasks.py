import celery
from celery.signals import task_postrun
from celery.utils.log import get_task_logger
import requests
import os

logger = get_task_logger(__name__)

@celery.task(name="put_to_api")
def put_to_api(session_id):
    #f=open("/heimdal/sess_id.txt",'w')
    #session_id=f.readlines()
    print(session_id)
    r = requests.put(os.environ.get('SB_HB_URL') + '/' + session_id)

@celery.task
def log(message):
    """Print some log messages"""
    logger.debug(message)
    logger.info(message)
    logger.warning(message)
    logger.error(message)
    logger.critical(message)

