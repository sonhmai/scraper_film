from flask import jsonify, request
from app.api import bp
from app.models import User
from app.api.errors import bad_request
from sqlalchemy import func
from app import db


# get all movies
@bp.route('/users', methods=['GET'])
def get_users():
    res = User.to_collection()
    return jsonify(res)


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
    payload = request.get_json() or {}
    # check if payload has enough fields
    if 'username' not in payload or 'password' not in payload:
        return bad_request('Must include fields: username and password.')
    if User.query.filter(func.lower(payload['username']) == func.lower(User.username)).first():
        return bad_request(f"Username {payload['username']} was already used.")
    user = User(username=payload['username'], password_hash=payload['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())


# delete a movie
@bp.route('/movies/<movie_id>', methods=['DELETE'])
def delete_user(movie_id):
    pass
