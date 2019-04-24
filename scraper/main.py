from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import requests


path_module = os.path.dirname(os.path.abspath(__file__))
# checking the OS app is running on
if os.name == 'nt':
    # running on windows, use driver for windows
    path_chromedriver = os.path.join(path_module, 'chromedriver.exe')
else:
    # can be 'java' or 'posix', but I only use posix so not checking for java here
    path_chromedriver = os.path.join(path_module, 'chromedriver2.44.exe')

movie_api = 'http://35.247.160.45/api/movies'


def get_movies_info(infos, session):
    """
    parses movie information (title, genre, start_date) from a list
    of Tag div (class='product-info')
    :param infos: list of bs4.element.Tag('div') containing movie info
    :return:
    """
    for info in infos:
        title = info.h2.string
        spans = info(name='span', class_='cgv-info-normal')
        # stripping whitespaces from beginning and end of result
        genre = spans[0].get_text(strip=True)
        start_date = spans[2].get_text(strip=True)
        # if any of the field is missing
        if not title or not genre or not start_date:
            print("Not enough info: title <{0}>, genre <{1}>, start_date <{2}>".format(title, genre, start_date))
            continue  # go to the next loop

        movie = {
            'title': title,
            'genre': genre,
            'start_date': start_date
        }

        response = requests.post(url=movie_api, json=movie)
        if response.status_code != 200:
            print(movie)
            print(response.status_code, response.content)
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


