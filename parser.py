import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def parse_magput(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        tour_elements = soup.select(".t-card")  # Исправленный селектор

        print(f"Найдено туров: {len(tour_elements)}", flush=True) # Проверка количества найденных элементов

        for tour_element in tour_elements:
            link_element = tour_element.find("a", target="_blank", href=True)
            direction_element = tour_element.find("div", class_="tcart__direction")


            if link_element and direction_element:
                link = "https://magput.ru" + link_element["href"]
                direction = direction_element.text.strip()
                print(f"Ссылка: {link}, Направление: {direction}", flush=True)
            else:
                print("Ошибка: не удалось найти ссылку или направление для одного из туров.", flush=True)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}", flush=True)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}", flush=True)


if __name__ == "__main__":
    url = "https://magput.ru/tours/india"
    parse_magput(url, headers)
