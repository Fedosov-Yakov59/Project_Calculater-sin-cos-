import telebot
from telebot import types
import threading
from Calculater import main  # Импортируем функцию main из файла калькулятора
import flet as ft

# Создаем экземпляр бота
API_TOKEN = '8125049217:AAFXtqLbWzp22Snc8a-s7DvOGUi36c1ynOw'
bot = telebot.TeleBot()

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
    # Запускаем калькулятор в отдельном потоке
    threading.Thread(target=run_calculator).start()

def run_calculator():
    ft.app(target=main)  # Запускаем приложение Flet

# Запуск бота
bot.polling() 
