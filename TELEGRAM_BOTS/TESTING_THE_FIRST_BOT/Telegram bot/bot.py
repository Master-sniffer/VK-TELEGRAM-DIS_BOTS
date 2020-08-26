import requests
import random
import telebot
from telebot.types import Message

TOKEN = ''

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):
    bot.reply_to(message,str(random.randint(0,100)))

bot.polling(timeout=60)
