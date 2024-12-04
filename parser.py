import requests
from bs4 import BeautifulSoup
import re

base_url = "https://vand.ru/country/india/"
tour_base_url = "https://vand.ru"


def parse_tour_page(tour_url):
    try:
        response = requests.get(tour_url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        soup = BeautifulSoup(response.content, "html.parser")

        title_element = soup.find("h1", class_="page-title h1")
        description_element = soup.find("div", class_="my-4 text-center")

        title = title_element.text.strip() if title_element else ""
        description = description_element.text.strip() if description_element else ""

        return title, description
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {tour_url}: {e}")
        return "", ""



def parse_page(page_url):
    try:
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        tour_links = soup.find_all("a", href=re.compile(r"/country/india/tour/"))

        for tour_link in tour_links:
            href = tour_link["href"]
            tour_url = tour_base_url + href
            title, description = parse_tour_page(tour_url)
            print(f"{tour_url},{title},{description}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {page_url}: {e}")


def main():
    page_num = 1
    while True:
      page_url = f"{base_url}?PAGEN_1={page_num}"
      response = requests.get(page_url)

      if response.status_code == 404: # Проверка на существование страницы
          break

      parse_page(page_url)
      page_num += 1



if __name__ == "__main__":
    main()
