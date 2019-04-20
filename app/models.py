from scraper import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True)
    genre = db.Column(db.String)
    start_date = db.Column(db.Date)

    def __repr__(self):
        return '<Movie %d, %s, %s, %s>' % (self.id, self.title, self.genre, self.start_date)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'start_date': self.start_date
        }

    @staticmethod
    def to_collection():
        movies = Movie.query.all()
        res = {
            'items': [
                movie.to_dict() for movie in movies
            ],
            '_meta': {
                'num': len(movies)
            }
        }
        return res


