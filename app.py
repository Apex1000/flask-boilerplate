from flask import Flask, request, jsonify,render_template, redirect, url_for,session,message_flashed,send_file,send_from_directory
# from models import Exams
import simplejson
import json
import random
import string
import uuid
import os
import urllib.request
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.secret_key = 'worldsucks'
engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'))
Session = sessionmaker(bind=engine)
ses = Session()

IMAGE_DIR = 'static/images'
app.config['IMAGE_DIR'] = IMAGE_DIR
# migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'OK',200

@app.route('/')
def index():
    return 'OK',200

@app.route('/')
def index():
    return 'OK',200

@app.route('/')
def index():
    return 'OK',200


if __name__ == '__main__':
    app.run(threaded=True, port=8000,debug=True)
