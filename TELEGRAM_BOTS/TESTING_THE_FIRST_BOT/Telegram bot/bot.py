import requests
import random
import telebot
from telebot.types import Message

TOKEN = ''
STICKER_ID='CAACAgIAAxkBAAN1X0aeJkafPIr1haxKJEvF1nRDPToAAsEAA2sLFBR5KCryovaX0xsE'

bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start",'help'])
def commands_and_handler(message:Message):
    bot.reply_to(message, "AYE")


@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):
    if 'alexa' in message.text:
        bot.reply_to(message,str("Pishov Nahui"))
        return 
    bot.reply_to(message,str(random.randint(0,100)))

@bot.message_handler(content_types=["sticker"])
def stickos (message:Message):
    bot.send_sticker(message.chat.id, STICKER_ID)

bot.polling(timeout=60)
