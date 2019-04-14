from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    start = db.Column(db.Date)
    genre = db.Column(db.String())


if __name__ == '__main__':
    movie = Movies(name='Pulp Fiction', genre='Drama,Action', start='2019-02-04')
    db.session.add(movie)
    db.commit()


