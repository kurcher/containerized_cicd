import telebot
import os
import threading
import time
import schedule
from datetime import datetime


BOT_TOKEN = os.getenv("BOT_TOKEN")    

bot = telebot.TeleBot(BOT_TOKEN)
user_data = {}
DAILY_GOAL = 2.0  


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    user_data[user_id] = {'drank': 0.0}
    bot.send_message(user_id, "👋 Привіт! Я буду нагадувати пити воду кожні 2.5 години!\n"
                              "Введи скільки води ти випив, наприклад: 0.3")


@bot.message_handler(commands=['progress'])
def handle_progress(message):
    user_id = message.chat.id
    drank = user_data.get(user_id, {}).get('drank', 0.0)
    bot.send_message(user_id, f"💧 Прогрес: {drank:.2f}/{DAILY_GOAL} л")


@bot.message_handler(func=lambda message: True)
def handle_water_input(message):
    user_id = message.chat.id
    try:
        amount = float(message.text.replace(",", "."))
        if amount <= 0:
            raise ValueError
        user_data.setdefault(user_id, {'drank': 0.0})
        user_data[user_id]['drank'] += amount
        total = user_data[user_id]['drank']
        bot.send_message(user_id, f"✅ Додано {amount:.2f} л. Всього: {total:.2f}/{DAILY_GOAL} л")
    except ValueError:
        bot.send_message(user_id, "🚫 Введи кількість у літрах, наприклад: 0.3")


def send_reminders():
    for user_id in user_data:
        bot.send_message(user_id, "🚰 Час пити воду!")


def reset_daily():
    for user_id in user_data:
        user_data[user_id]['drank'] = 0.0
        bot.send_message(user_id, "🕛 Новий день! Лічильник обнулено.")


def schedule_runner():
    schedule.every(2.5).hours.do(send_reminders)
    schedule.every().day.at("00:00").do(reset_daily)

    while True:
        schedule.run_pending()
        time.sleep(1)


threading.Thread(target=schedule_runner, daemon=True).start()

bot.polling()
