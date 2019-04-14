import sqlalchemy
from model import Movie


db = 'sqlite:///app.db'
engine = sqlalchemy.create_engine(db)
Session = sqlalchemy.orm.sessionmaker(bind=engine)


def create_table():
    # check if table exists
    if not engine.dialect.has_table(engine, 'movie'):
        Movie.__table__.create(engine)
    else:
        print('Table already exists.')


if __name__ == '__main__':
    session = Session()
    create_table()
