import requests
from bs4 import BeautifulSoup

base_url = "https://www.otkrytie.ru/india"
tour_base_url = "https://www.otkrytie.ru"

def parse_tour_page(tour_url):
    try:
        response = requests.get(tour_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        country_element = soup.find("span", class_="tour-country")
        route_element = soup.find("h4", class_="box-title", text="Маршрут тура").find_next_sibling("p")


        country = country_element.text.strip() if country_element else "Страна не найдена"
        route = route_element.text.strip() if route_element else "Маршрут не найден"

        return country, route

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {tour_url}: {e}")
        return None, None
    except AttributeError as e:
        print(f"Ошибка парсинга страницы {tour_url}: {e}")
        return None, None



def parse_page(page_url):
    try:
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        tour_links = soup.find_all("div", class_="box-title h-4") # Изменение здесь


        for tour_link in tour_links:
             href = tour_link.find('a', href=True)['href'] 
             if href:  # Проверка на существование ссылки
                tour_url = tour_base_url + href
                country, route = parse_tour_page(tour_url)
                if country and route: # проверка на None 
                    print(f"URL: {tour_url}, Страна: {country}, Маршрут: {route}")


    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {page_url}: {e}")


def main():
    parse_page(base_url)  # Парсим только указанную страницу



if __name__ == "__main__":
    main()
