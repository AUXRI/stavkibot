import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["betboom_db"]
collection = db["matches"]

def fetch_data():
    url = "https://betboom.ru/sport/Upcoming/19879#SportEvents/19879"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Пример извлечения данных, это зависит от структуры сайта
    players = soup.find_all('div', class_='player-name')
    score = soup.find('div', class_='score')
    odds = soup.find('div', class_='odds')

    data = {
        "player_1": players[0].text,
        "player_2": players[1].text,
        "score": score.text,
        "odds": odds.text
    }

    # Сохранение в MongoDB
    collection.update_one({"_id": data["player_1"] + " vs " + data["player_2"]}, {"$set": data}, upsert=True)

fetch_data()
