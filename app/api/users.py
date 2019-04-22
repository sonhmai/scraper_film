from flask import jsonify, request
from app.api import bp
from app.models import User
from app.api.errors import bad_request
from sqlalchemy import func
from datetime import datetime
from app import db


# get all movies
@bp.route('/users', methods=['GET'])
def get_users():
    return 'getting all users'


# get 1 movies by id
@bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    pass


# update a movie by id, PUT = whole movie entity must be supplied by client
@bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    pass


# create a new user
@bp.route('/users', methods=['POST'])
def create_user():
    return 'creating user'


# delete a movie
@bp.route('/movies/<movie_id>', methods=['DELETE'])
def delete_user(movie_id):
    pass
