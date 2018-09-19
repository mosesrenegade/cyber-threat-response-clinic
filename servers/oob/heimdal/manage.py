#!/usr/bin/env python
import os
from flask import Flask, current_app
from flask_script import Manager, Server
from flask_migrate import Migrate
import config
from app import create_app

manager = Manager(create_app)

manager.add_command("server", Server(host='0.0.0.0', port=5000))

@manager.shell
def make_shell_context():
    return dict(app=create_app)

if __name__ == "__main__":
    manager.run()
