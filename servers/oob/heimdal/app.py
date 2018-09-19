import os
from flask import Flask, render_template, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from celery import Celery
from celery.signals import task_postrun
from celery.utils.log import get_task_logger
import celeryconfig
from config import config
import xml.etree.ElementTree as ET
import tasks

session_id=''

def get_systems(systems):
    name = ''
    ip_address = ''
    status = ''
    #try:

    hosts_new = list(mongo.db.servers.find())
        
    #except (SQLAlchemy.exc.SQLAlchemyError, SQLAlchemy.exc.DBAPIError) as e:
    #    e.append('unable to query the database')
    #    return { 'error': e }

    return hosts_new

def get_sessionid(session_id):
    if os.environ['FLASK_ENV'] == 'development':
        guacfile = 'user-mapping.xml'
    else:
        try:
            guacfile = '/etc/guacamole/user-mapping.xml'
        finally:
            guacfile = 'user-mapping.xml'
            pass
    
    tree = ET.parse(guacfile)
    root = tree.getroot()
    for child in root:
        session_id = child.attrib['password']
        if os.environ['FLASK_ENV'] == 'development':
            print("session_id for this session is: " + session_id)
    f=open('sess_id.txt','w')
    f.write(session_id)
    f.close
    return session_id

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['BROKER_URL']
    )

    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery

def create_app(config=None):
    hosts = ''
    systems = ''
    app = Flask(__name__, instance_relative_config=True)
    app.debug = False
    app.config.from_object(os.environ['APP_SETTINGS'])
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/heimdal'

    #db.init_app(app)
    
    @app.route('/')
    def index():
        return render_template('index.html', hosts=get_systems(systems), sess = get_sessionid(session_id))
    
    return app


#db = SQLAlchemy()
#import models

app = create_app()

celery = make_celery(app)
mongo = PyMongo(app)


# Lets make some celery tasks on boot
try:
    tasks.put_to_api(get_sessionid(session_id))
except:
    pass
    
if __name__ == 'main':
    app.run(host='0.0.0.0')
