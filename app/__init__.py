import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy

app = Flask(__name__)
db_path = 'sqlite:///' + os.path.dirname(os.path.dirname(__file__)) + '/app.db'
db_cloudsql = sqlalchemy.engine.url.URL(
    drivername='mysql+pymysql',
    username='root',
    password='2471',
    database='film_scraper',
    query={'unix_socket': 'cloudsql/{}'.format('compact-works-233401:asia-southeast1:movies-scraper')
    }
)

db_cloudsql = 'mysql+pymysql://root:2471@35.198.211.146/film_scraper'
app.config['SQLALCHEMY_DATABASE_URI'] = db_cloudsql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.api.movies import bp as api_blueprint

from app.models import Movie

from app import routes  # register main routes
from app.api import movies  # register the api-movies routes
from app.api import users
app.register_blueprint(api_blueprint, url_prefix='/api')
