from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from app.api import bp as api_blueprint

from app.models import Movie

from app import routes  # register main routes
from app import api  # register the api routes
app.register_blueprint(api_blueprint, url_prefix='/api')
