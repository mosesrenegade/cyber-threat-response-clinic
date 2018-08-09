#!flask/bin/python
import os
import redis
from flask import Flask, render_template, jsonify, url_for, request
from celery import Celery
import xml.etree.ElementTree as ET

app = Flask(__name__)
if os.environ['FLASK_ENV'] == 'development':
    dev = True
else:
    dev = False

db = redis.Redis('localhost') 

@app.route('/', methods = ['GET'])
def index():
    sessions = {}
    
    return render_template('index.html', sessions=sessions)

@app.route('/session', methods = ['GET', 'POST'])
def session():
    req_data = request.json

    try:
        session_id = req_data['sess']
    except:
        print(session_id)
    return_template('sessions.html', sessions=sessions)
    
if __name__=='__main__':
    if os.environ['FLASK_ENV'] == 'development':
        app.run(debug=True, port=5001)
    else:
        app.run(debug=False)
