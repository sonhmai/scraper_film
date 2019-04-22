from flask import jsonify, Blueprint, request
bp = Blueprint('api', __name__)

from app.models import Movie
from app.api.errors import bad_request
from sqlalchemy import func
from datetime import datetime
from app import db


# get all movies
@bp.route('/movies', methods=['GET'])
def get_movies():
    res = Movie.to_collection()
    return jsonify(res)


# get 1 movies by id
@bp.route('/movies/<movie_id>', methods=['GET'])
def get_movie(movie_id):
    # can use get instead of filter_by for primary key
    # res = Movie.query.filter_by(id=movie_id).first().to_dict()
    res = Movie.query.get_or_404(movie_id).to_dict()
    return jsonify(res)


# update a movie by id, PUT = whole movie entity must be supplied by client
@bp.route('/movies/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    payload = request.get_json() or {}
    # verify that the request must have field title, genre, start_date
    if 'title' not in payload or 'genre' not in payload or 'start_date' not in payload:
        return bad_request('not valid. json body must include: title, genre, start_date.')
    movie = Movie.query.get_or_404(movie_id)
    movie.title = payload['title']
    movie.genre = payload['genre']
    # movie.start_date accepts Python date obj
    payload['start_date'] = datetime.strptime(payload['start_date'], '%d-%m-%Y').date()
    movie.start_date = payload['start_date']
    db.session.commit()
    return jsonify(movie.to_dict())


# create a new movie
@bp.route('/movies', methods=['POST'])
def create_movie():
    # or {} to prevent payload==None causing payload not iterable error
    payload = request.get_json() or {}
    # verify that the request must have field title, genre, start_date
    if 'title' not in payload or 'genre' not in payload or 'start_date' not in payload:
        return bad_request('not valid. json body must include: title, genre, start_date.')

    # if title already exists, return error
    # filter_by returns a query object, first() returns 1st result or None
    title = payload['title']
    # use filter and func for case-insensitive check
    if Movie.query.filter(func.lower(Movie.title) == func.lower(title)).first():
        return bad_request(f"Title {title} was used already. Choose another.")

    # change date string from POST request to python date object
    payload['start_date'] = datetime.strptime(payload['start_date'], '%d-%m-%Y').date()
    # create Movie object from the dict
    movie = Movie(title=title, genre=payload['genre'], start_date=payload['start_date'])
    # add Movie object to session
    db.session.add(movie)
    db.session.commit()
    # return created object with successful code
    return jsonify(movie.to_dict())


# delete a movie
@bp.route('/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return f'delete movie_id: {movie_id}'
