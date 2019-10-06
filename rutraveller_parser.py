import logging

import requests
from bs4 import BeautifulSoup


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='rutravveler_parse.log')


def get_html(url, page_num):
    try:
        page = requests.get(f'{url}/{page_num}')
        page.raise_for_status()
        return page.text
    except requests.RequestException:
        logging.info('404 found at %s/%d', url, page_num)
        return False


def get_places(url, page_num=1):
    logging.info('Parsing started')
    errors_count = 0
    while True:
        page_html = get_html(url, page_num)
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
            logging.info('page %s/%d not verified, skipping', url, page_num)
            continue
        name = soup.find('h1', class_='title-h1').text
        description = soup.find('div', class_='place-description').find('div', class_='text').text
        location = soup.find('span', class_='info-line__text_gray').text
        place_info = {
            'place_name': name,
            'place_description': description,
            'location': location
        }
        print(f'{place_info["location"]}')


if __name__ == "__main__":
    get_places('https://rutraveller.ru/place')
