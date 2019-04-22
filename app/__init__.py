import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db_path = 'sqlite:///' + os.path.dirname(os.path.dirname(__file__)) + '/app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.api.movies import bp as api_blueprint

from app.models import Movie

from app import routes  # register main routes
from app.api import movies  # register the api-movies routes
app.register_blueprint(api_blueprint, url_prefix='/api')
