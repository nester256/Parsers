import requests
from bs4 import BeautifulSoup
import lxml
import time

products = {}
for i in range(1, 24):
    params = {
        'p': str(i),
    }
    time.sleep(1)
    print(f"собираю данные со страницы {i}")
    # response = requests.get('https://sochi.technopark.ru/smartfony/',params=params, cookies=cookies, headers=headers)
    response = requests.get('https://sochi.technopark.ru/smartfony/', params=params)
    print(response)
    soup = BeautifulSoup(response.text, "lxml")
    container = soup.find("div", class_="catalog-listing")
    cards = container.find_all("div", class_="product-card-big__container")
    for card in cards:
        name = card.find("div", class_="product-card-big__name").text.strip()
        price = card.find("div", class_="product-prices__price").text.strip()[:7]
        products[name] = price
print(products)
