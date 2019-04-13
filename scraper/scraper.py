from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def get_movies_info(infos):
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
        print("genre:", genre)
        print("start_date:", start_date)
        print('--------------')


webdriver_path = './chromedriver.exe'
# add args to tell Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
# open browser
browser = webdriver.Chrome(executable_path=webdriver_path, chrome_options=chrome_options)

url_phimsapchieu = 'https://www.cgv.vn/default/movies/coming-soon-1.html'
browser.get(url_phimsapchieu)
time.sleep(0.1)  # wait for page to load

soup = BeautifulSoup(browser.page_source, features='html.parser')
# print(soup.prettify())  # debugging

infos = soup.find_all(name='div', class_='product-info')
if len(infos) == 0:
    print('cannot find tag.')
else:
    get_movies_info(infos)
