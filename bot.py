import telebot
from pymongo import MongoClient
from telebot import types


TOKEN = "7225973611:AAFrW1gFKB4_A7F-jLvW95b69FbOrUfbh14"
bot = telebot.TeleBot(TOKEN)

client = MongoClient("mongodb://localhost:27017/")
db = client["betboom_db"]
users = db["users"]

@bot.message_handler(commands=['start', 'register'])
def send_welcome(message):
    chat_id = message.chat.id
    user = users.find_one({"chat_id": chat_id})
    if user:
        bot.send_message(chat_id, "Вы уже зарегистрированы!")
    else:
        users.insert_one({"chat_id": chat_id, "username": message.from_user.username})
        bot.send_message(chat_id, "Регистрация прошла успешно!")

@bot.message_handler(commands=['score'])
def send_score(message):
    chat_id = message.chat.id
    match = collection.find_one(sort=[('_id', -1)])  # Последний матч
    if match:
        bot.send_message(chat_id, f"{match['player_1']} vs {match['player_2']}\nСчет: {match['score']}\nКоэффициент: {match['odds']}")
    else:
        bot.send_message(chat_id, "Данные о матче отсутствуют.")

bot.polling()
