from flask import jsonify, Blueprint
bp = Blueprint('api', __name__)

from app.models import Movie


@bp.route('/movies', methods=['GET'])
def get_movies():
    res = Movie.to_collection()
    return jsonify(res)

