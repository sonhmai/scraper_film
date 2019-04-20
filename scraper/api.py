from scraper import app
from flask import jsonify
from scraper.app import Movie


@app.route('/')
def home():
    return 'hello, world'


@app.route('/api/movie', methods=['GET'])
def get_movies():
    res = Movie.to_collection()
    return jsonify(res)