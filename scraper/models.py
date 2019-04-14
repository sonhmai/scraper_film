from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    genre = Column(String)
    start_date = Column(Date)

