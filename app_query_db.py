from scraper.models_old import Movie
from scraper import Session


session = Session()
res = session.query(Movie).all()
print(len(res))
for movie in res:
    print(movie.title)
