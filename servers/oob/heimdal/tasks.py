import celery
from celery.signals import task_postrun
from celery.utils.log import get_task_logger
import requests

logger = get_task_logger(__name__)

@celery.task(name="put_to_api")
def put_to_api(session_id):
    print(session_id)    
    r = requests.put('http://localhost:5555', data={'session_id':session_id})
    
@celery.task
def log(message):
    """Print some log messages"""
    logger.debug(message)
    logger.info(message)
    logger.warning(message)
    logger.error(message)
    logger.critical(message)

