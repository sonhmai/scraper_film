import time
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scraper.main import get_movies_info, get_browser
from app import db_cloudsql


if __name__ == '__main__':
    browser = get_browser()
    url_phimsapchieu = 'https://www.cgv.vn/default/movies/coming-soon-1.html'
    browser.get(url_phimsapchieu)
    time.sleep(0.1)  # wait for page to load

    # db sesion
    engine = create_engine(db_cloudsql)
    Session = sessionmaker(bind=engine)
    session = Session()

    soup = BeautifulSoup(browser.page_source, features='html.parser')
    # print(soup.prettify())  # debugging
    infos = soup.find_all(name='div', class_='product-info')
    if len(infos) == 0:
        print('cannot find tag.')
    else:
        get_movies_info(infos, session)
        session.commit()
