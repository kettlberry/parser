import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

def parse_magput(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        tour_cards = soup.find_all("div", class_="tcart__item") # находим все карточки туров

        for card in tour_cards:
            tour_link_element = card.find("a", target="_blank", href=True)
            direction_element = card.find("div", class_="tcart__direction").find("a", href=True)


            if tour_link_element and direction_element:
                tour_link = "https://magput.ru" + tour_link_element["href"]
                direction_link = "https://magput.ru" + direction_element["href"]
                direction_text = direction_element.get_text(strip=True)

                print(f"Ссылка на тур: {tour_link}")
                print(f"Ссылка на направление: {direction_link}")
                print(f"Название направления: {direction_text}")
                print("-" * 20)
            else:
                print("Ошибка: не удалось найти ссылку на тур или направление в одной из карточек.")


    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    url = "https://magput.ru/tours/india"
    parse_magput(url, headers)
