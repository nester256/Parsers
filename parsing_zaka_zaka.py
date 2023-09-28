import json
from time import sleep
from bs4 import BeautifulSoup

import requests


cookies = {
    'PHPSESSID': '2ifsuf4k6ku72g6vfufldc4ot6',
    '51a55dae53577255b792d39bfe1d40ac': '0',
    '_ga': 'GA1.1.162462848.1695899742',
    '_ym_uid': '1695899744794178473',
    '_ym_d': '1695899744',
    '_ym_isad': '1',
    '_ga_BB3QC8QLF4': 'GS1.1.1695924306.2.1.1695926882.0.0.0',
}

headers = {
    'authority': 'zaka-zaka.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=2ifsuf4k6ku72g6vfufldc4ot6; 51a55dae53577255b792d39bfe1d40ac=0; _ga=GA1.1.162462848.1695899742; _ym_uid=1695899744794178473; _ym_d=1695899744; _ym_isad=1; _ga_BB3QC8QLF4=GS1.1.1695924306.2.1.1695926882.0.0.0',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition Yx GX)',
}


games = {}
for i in range(1, 15):
    sleep(1)
    response = requests.get(f'https://zaka-zaka.com/game/new/page{i}', cookies=cookies, headers=headers)
    print(f'Страница {i} {response}')
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.find_all('a', class_='game-block')
    for game in container:
        name = game.find('div', class_='game-block-name').text
        price = game.find('div', class_='game-block-price').text.replace('c', "RUB")
        games[name] = price
with open("games.json", "w") as json_file:
    json.dump(games, json_file)
