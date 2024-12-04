import requests
from bs4 import BeautifulSoup

def parse_magput(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        tour_elements = soup.find_all("div", class_="tcart js-tour-list-item")  # Находим все блоки с турами

        for tour_element in tour_elements:
            link_element = tour_element.find("a", target="_blank", href=True)
            direction_element = tour_element.find("div", class_="tcart__direction")


            if link_element and direction_element:
                link = link_element["href"]
                direction = direction_element.text.strip()
                print(f"Ссылка: {link}, Направление: {direction}")
            else:
                print("Ошибка: не удалось найти ссылку или направление для одного из туров.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")



if __name__ == "__main__":
    url = "https://magput.ru/tours/india"
    parse_magput(url)
