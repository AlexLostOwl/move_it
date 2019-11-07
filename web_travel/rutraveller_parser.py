import logging
import requests
from bs4 import BeautifulSoup

from web_travel import (save_place, save_country, save_city, save_photo,
                        place_exists, city_exists)

URL = 'https://rutraveller.ru/place'


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='rutraveler_parse.log')


def get_html(url, page_num):
    try:
        page = requests.get(f'{url}/{page_num}')
        page.raise_for_status()
        return page.text
    except requests.RequestException:
        logging.info('404 found at %s/%d', url, page_num)
        return False


def get_places(page_num=1):
    logging.info('Parsing started')
    errors_count = 0
    while True:
        page_html = get_html(URL, page_num)
        page_num += 1
        if errors_count == 4 and not page_html:
            logging.info('Pages with 404 error were %d in a row. Stop parsing', errors_count + 1)
            break
        if not page_html:
            errors_count += 1
            continue
        errors_count = 0
        soup = BeautifulSoup(page_html, 'html.parser')
        if soup.find('span', class_='label-status--notverified'):
            logging.info('page %s/%d not verified, skipping', URL, page_num)
            continue
        name = soup.find('h1', class_='title-h1').text
        description = soup.find('div', class_='place-description').find('div', class_='text').text
        location = soup.find('span', class_='info-line__text_gray').text.split(', ')
        country = location[-1]
        photos = []
        for img in soup.find_all('div', class_='photo-tile__cover'):
            photos.append(img.find('img').get('src'))
        if place_exists(name, country):
            continue
        else:
            save_country(country)
            if len(location) >= 2:
                city = location[-2]
                if not city_exists(city, country):
                    save_city(city, country)
            else:
                city = None
            save_place(name, description, country, city)
            for img in photos:
                save_photo(img, name)


if __name__ == "__main__":
    get_places()
