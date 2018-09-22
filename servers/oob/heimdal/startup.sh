#!/bin/bash

cd /heimdal

FLASK_ENV='production'
python3 ./manage.py server
