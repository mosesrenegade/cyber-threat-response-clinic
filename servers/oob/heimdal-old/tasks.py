from celery.signals import task_postrun
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery.task
def log(message):
    """Print some log messages"""
    logger.debug(message)
    logger.info(message)
    logger.warning(message)
    logger.error(message)
    logger.critical(message)
