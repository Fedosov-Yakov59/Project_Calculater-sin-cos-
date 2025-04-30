import telebot
from telebot import types
import multiprocessing
import sqlite3
from Calculater import main  # Импортируем функцию main из файла калькулятора
import flet as ft

# Создаем экземпляр бота
API_TOKEN = '8125049217:AAFXtqLbWzp22Snc8a-s7DvOGUi36c1ynOw'  # Замените на ваш токен
bot = telebot.TeleBot(API_TOKEN)

# Создаем или подключаемся к базе данных
conn = sqlite3.connect('suggestions.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS suggestions (id INTEGER PRIMARY KEY, suggestion TEXT)''')
conn.commit()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    calculator_button = types.KeyboardButton("Калькулятор")
    suggest_button = types.KeyboardButton("Предложить новые функции")
    markup.add(calculator_button, suggest_button)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

# Обработчик нажатия кнопки "Калькулятор"
@bot.message_handler(func=lambda message: message.text == "Калькулятор")
def start_calculator(message):
    bot.send_message(message.chat.id, "Запускаем калькулятор...")
    # Запускаем калькулятор в отдельном процессе
    multiprocessing.Process(target=run_calculator).start()

def run_calculator():
    ft.app(target=main)  # Запускаем приложение Flet

# Обработчик нажатия кнопки "Предложить новые функции"
@bot.message_handler(func=lambda message: message.text == "Предложить новые функции")
def suggest_feature(message):
    bot.send_message(message.chat.id, "Хорошо, напишите её! И Ваша функция будет рассмотрена!")

    # Устанавливаем состояние ожидания предложения
    bot.register_next_step_handler(message, save_suggestion)

def save_suggestion(message):
    suggestion = message.text
    # Сохраняем предложение в базе данных
    cursor.execute("INSERT INTO suggestions (suggestion) VALUES (?)", (suggestion,))
    conn.commit()
    bot.send_message(message.chat.id, "Спасибо большое за помощь!")

# Запуск бота
if __name__ == "__main__":
    bot.polling()
