import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = 6379
    BROKER_URL = os.environ.get('REDIS_URL', "redis://{host}:{port}/0".format(host=REDIS_HOST, port=str(REDIS_PORT)))
    CELERY_RESULT_BACKEND = BROKER_URL
    
class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'postgresql://dev:dev@localhost:5432/heimdal'

class ProductionConfig(Config):
    DEBUG = False
    
config = {
    'development': DevelopmentConfig
}
