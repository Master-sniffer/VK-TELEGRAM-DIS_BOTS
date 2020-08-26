import requests
import random
import pickle
import telebot
from telebot.types import Message
from telebot import types

TOKEN = '1379710116:AAG9BmigUQlgZKnQ3_JEWqKo--7HbbiF1O0'
STICKER_ID='CAACAgIAAxkBAAN1X0aeJkafPIr1haxKJEvF1nRDPToAAsEAA2sLFBR5KCryovaX0xsE' # найдите стикос по души и отправляйте его :)

bot=telebot.TeleBot(TOKEN)

USERS=set()  # Юзаем множество вместо словаря 

@bot.message_handler(commands=["start",'help'])
def commands_and_handler(message:Message):
    bot.reply_to(message, "AYE")


@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):
    reply=str(random.randint(0,100))

    if 'alexa' in message.text:
        bot.reply_to(message,str("Pishov Nahui"))
        return 
    if message.from_user.id in USERS:
        reply+=f" {message.from_user.first_name} thats your new number" 
    else:
        USERS.add(message.from_user.id)
    bot.reply_to(message,reply)


@bot.message_handler(content_types=["sticker"])
def stickos (message:Message):
    bot.send_sticker(message.chat.id, STICKER_ID)

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    print (inline_query)
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

bot.polling(timeout=60)
