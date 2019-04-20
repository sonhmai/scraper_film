from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from scraper.models_old import Movie
from datetime import datetime


path_module = os.path.dirname(os.path.abspath(__file__))
path_chromedriver = os.path.join(path_module, 'chromedriver2.44.exe')


def get_movies_info(infos, session):
    """
    parses movie information (title, genre, start_date) from a list
    of Tag div (class='product-info')

    :param infos: list of bs4.element.Tag('div') containing movie info
    :return:
    """
    for info in infos:
        title = info.h2.string
        print(title)
        spans = info(name='span', class_='cgv-info-normal')
        # stripping whitespaces from beginning and end of result
        genre = spans[0].get_text(strip=True)
        start_date = spans[2].get_text(strip=True)
        start_date = datetime.strptime(start_date, '%d-%m-%Y').date()  # convert to date obj
        # create record
        movie = Movie(title=title, genre=genre, start_date=start_date)
        session.add(movie)
        print('--------------')


def get_browser():
    # add args to tell Selenium to not actually open a window
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')
    # open browser
    browser = webdriver.Chrome(executable_path=path_chromedriver,
                               chrome_options=chrome_options)
    return browser


