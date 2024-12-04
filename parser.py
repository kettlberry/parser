import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def parse_magput(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        tour_elements = soup.select(".tcart__in")  # Выбираем блоки с турами

        print(f"Найдено блоков с турами: {len(tour_elements)}", flush=True)

        for tour_element in tour_elements:
            link_element = tour_element.find("a", target="_blank", href=True)
            direction_element = tour_element.find("div", class_="tcart__direction").find("a", href=True)

            if link_element and direction_element:
                link = "https://magput.ru" + link_element["href"]
                direction_link = "https://magput.ru" + direction_element["href"] # Формируем ссылку на направление
                direction_text = direction_element.text.strip() # Получаем текст направления

                print(f"Ссылка на тур: {link}", flush=True)
                print(f"Ссылка на направление: {direction_link}", flush=True)
                print(f"Текст направления: {direction_text}", flush=True)
                print("-" * 20, flush=True) # Разделитель между турами

            else:
                print("Ошибка: не удалось найти ссылку или направление для одного из туров.", flush=True)


    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}", flush=True)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}", flush=True)


if __name__ == "__main__":
    url = "https://magput.ru/tours/india"
    parse_magput(url, headers)
