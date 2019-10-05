import logging

import requests
from bs4 import BeautifulSoup


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='rutravveler_parse.log')


def get_html(url, page_num=0):
    while True:
        page_num += 1
        try:
            page = requests.get(f'{url}/{page_num}')
            page.raise_for_status()
            errors_count = 0
            yield page.text
        except requests.RequestException:
            logging.info('404 found at %s/%d', url, page_num)
            if errors_count == 3:
                logging.INFO('Pages with 404 error were %d in a row. Stop parsing', page_num)
                break
            else:
                errors_count += 1
                continue


def get_places(url):
    logging.info('Parsing started')
    for page_html in get_html(url, page_num=5):
        soup = BeautifulSoup(page_html, 'html.parser')
        name = soup.find('h1', class_='title-h1').text
        description = soup.find('div', class_='place-description').find('div', class_='text').text
        place_info = {
            'place_name': name,
            'place_description': description
        }
        print(f'{place_info["place_name"]}')


if __name__ == "__main__":
    get_places('https://rutraveller.ru/place')
