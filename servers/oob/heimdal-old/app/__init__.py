#!flask/bin/python
import os

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
import celeryconfig
import xml.etree.ElementTree as ET
import json
from config import config

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

from . import models
    
session_id = []
is_up = ''
systems = {}
dev = 1

def get_sessionid():
    if dev:
        guacfile='../user-mapping.xml'
    else:
        guacfile='/etc/guacamole/user-mapping.xml'
    tree = ET.parse(guacfile)
    root = tree.getroot()
    for child in root:
        session_id = child.attrib['password']
        if dev:
            print(session_id)
    return session_id

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['BROKER_URL']
    )

    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)


    celery.Task = ContextTask

    return celery

   
#def ping_systems(is_up):
#    for response in hosts:
#        os.system("ping -c 1" + response['address'])
#        if response == 0:
#            return is_up == True
#        else:
#            return is_up == False

def get_hosts(systems):
    
    if dev:
        #hosts = ['localhost', '127.0.0.1']
        #hosts = [{ 'id':'1', 'name': 'localhost', 'address': '127.0.0.1', 'is_up': ping_systems(is_up)},
        #{ 'id': '2', 'name':'127.0.0.1', 'address': '127.0.0.1', 'is_up': ping_systems(is_up)}]
        hosts = [{ 'id':'1', 'name':'localhost', 'address':'127.0.0.1' },
                 { 'id':'2', 'name':'127.0.0.1', 'address':'127.0.0.1' }]
    else:
        hosts = ['jumphost', 'ise', 'fmc', 'www']
    return hosts
            
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    #app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    
    @app.route('/', methods = ['GET'])
    @app.route('/index', methods = ['GET'])
    def index():
        if dev:
            #hosts = {'localhost', '127.0.0.1'}
            #hosts = get_hosts(systems)
            hosts = db.Result()
            print(hosts)
        else:
            hosts = {'fmc', 'jumphost'}

        return render_template('index.html', title='index', sess=get_sessionid(), hosts=hosts)

    return app

#flask_app = create_app(config_name)
#celerey = make_celery(flask_app)

#@app.route('/')
#def template_main():
    
#    h = get_hosts(systems)
#    for item in h:
#        id = item['id']
#        name = item['name']
#        address = item['address'] 
    
#    return render_template('index.html', title='index', sess=get_sessionid(), hosts=h)

#@app.route('/status')
#def status():
#    return render_template('status.html', title='status', jumphost_status=jumphost_status)
        

#if __name__=='__main__':
#    app.run()
