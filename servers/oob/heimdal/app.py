#!flask/bin/python
import os
from flask import Flask, render_template
from celery import Celery
import xml.etree.ElementTree as ET

app = Flask(__name__)
if os.environ['FLASK_ENV'] == 'development':
    dev = True
else:
    dev = False
    
session_id = []

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

@app.route('/')
def template_main(): 
    return render_template('index.html', title='index', sess=get_sessionid())
        

if __name__=='__main__':
    if os.environ['FLASK_ENV'] == 'development':
        app.run(debug=True)
    else:
        app.run(debug=False)
