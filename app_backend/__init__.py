import os
import sys
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, basedir)

from flask import Flask
from flask_appconfig import AppConfig
# Create the Flask instance
app = Flask('immo')
# Setup the configuration
AppConfig(app, os.path.join(basedir, 'default_config.py'))

from flask_restful import Api
api = Api(app)

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# Set the database connections
db = SQLAlchemy(app)
# Database migration engine
migrations_dir = basedir + '/../models/migrations'
migrate = Migrate(app, db, directory=migrations_dir)
# Manager of the app
manager = Manager(app)
# Add the command for the database
manager.add_command('db', MigrateCommand)

import ping
