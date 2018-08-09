#!flask/bin/python
import os
from flask import Flask, render_template, jsonify
from celery import Celery
import xml.etree.ElementTree as ET
import json

app = Flask(__name__)
try: 
    if os.environ['FLASK_ENV'] == 'development':
        dev = True
    else:
        dev = False
except:
    dev = False
    
session_id = []
is_up = ''
systems = {}

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

def ping_systems(is_up):
    for response in hosts:
        os.system("ping -c 1" + response['address'])
        if response == 0:
            return is_up == True
        else:
            return is_up == False

def get_hosts(systems):
    if dev:
        #hosts = ['localhost', '127.0.0.1']
        hosts = [{ 'id':'1', 'name': 'localhost', 'address': '127.0.0.1', 'is_up': ping_systems(is_up)},
        { 'id': '2', 'name':'127.0.0.1', 'address': '127.0.0.1', 'is_up': ping_systems(is_up)}]
    else:
        hosts = ['jumphost', 'ise', 'fmc', 'www']
    return hosts
            
@app.route('/')
def template_main():
    
    h = get_hosts(systems)
#    for item in h:
#        id = item['id']
#        name = item['name']
#        address = item['address'] 
    
    return render_template('index.html', title='index', sess=get_sessionid(), hosts=h)

#@app.route('/status')
#def status():
#    return render_template('status.html', title='status', jumphost_status=jumphost_status)
        

if __name__=='__main__':
    if os.environ['FLASK_ENV'] == 'development':
        app.run(debug=True)
    else:
        app.run(debug=False)
