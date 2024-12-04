import requests
from bs4 import BeautifulSoup
import re

base_url = "https://vand.ru/country/india/"
tour_base_url = "https://vand.ru"

def parse_tour_page(tour_url):
    # ... (Код этой функции без изменений)

def parse_page(page_url):
    # ... (Код этой функции без изменений)

def main():
    page_num = 1
    while True:
        page_url = f"{base_url}?PAGEN_1={page_num}"
        response = requests.get(page_url)

        if response.status_code == 404:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        pagination_block = soup.find('div', class_='bx-pagination-container')
        if pagination_block:
            next_link = pagination_block.find('li', class_='bx-pag-next')
            if not next_link or not next_link.find('a'):
                parse_page(page_url)
                break

        parse_page(page_url)
        page_num += 1

if __name__ == "__main__": # <-- Исправлено: добавлено 4 пробела перед кодом блока
    main()
