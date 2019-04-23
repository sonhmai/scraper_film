from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, index=True, unique=True)
    password_hash = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }

    @staticmethod
    def to_collection():
        users = User.query.all()
        res = {
            'items': [
                user.to_dict() for user in users
            ],
            '_meta': {
                'num': len(users)
            }
        }
        return res


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


