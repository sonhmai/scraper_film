import sqlalchemy
from models import Movie


db = 'sqlite:///app.db'
engine = sqlalchemy.create_engine(db)
Session = sqlalchemy.orm.sessionmaker(bind=engine)


if __name__ == '__main__':
    session = Session()
    res = session.query(Movie).all()
    print(len(res))
    for movie in res:
        print(movie.title)
