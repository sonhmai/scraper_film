from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
import sqlalchemy
import datetime


Base = declarative_base()
db_path = 'sqlite:///app.db'
engine = sqlalchemy.create_engine(db_path)
Session = sqlalchemy.orm.sessionmaker(bind=engine)


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    start = Column(Date)
    genre = Column(String())


if __name__ == '__main__':
    session = Session()
    start_date = datetime.date(2019, 2, 24)
    movie = Movie(name='Pulp Fiction', genre='Drama,Action', start=start_date)
    session.add(movie)
    session.commit()

