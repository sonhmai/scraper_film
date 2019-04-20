from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


path_module = os.path.dirname(os.path.abspath(__file__))
path_db = os.path.join(path_module, 'app.db')
db = 'sqlite:///' + path_db  # on windows using 3 slashes as there is no root for
# absolute path (4 slashes)
engine = create_engine(db)
Session = sessionmaker(bind=engine)

from scraper.models_old import Movie

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.api import bp as api_blueprint
app.register_blueprint(api_blueprint)