import requests
import json
import random
import pickle
import telebot
from telebot.types import Message
from telebot import types

TOKEN = '1379710116:AAG9BmigUQlgZKnQ3_JEWqKo--7HbbiF1O0'
STICKER_ID='CAACAgIAAxkBAAN1X0aeJkafPIr1haxKJEvF1nRDPToAAsEAA2sLFBR5KCryovaX0xsE' # найдите стикос по души и отправляйте его :)

bot=telebot.TeleBot(TOKEN)

USERS=set()  # Юзаем множество вместо словаря 


@bot.message_handler(commands=["music",'info', "meme"])
def commands_and_handler(message:Message):
    if message.text == "/music":
        bot.reply_to(message, "Hey, bro, listen to my music")
        music_i=["фвффвфв.mp3","ыыыы.mp3",'wait.mp3','is it you.mp3','ьфлы.mp3','ифи.mp3','Bass drive_1.mp3','silence.mp3']
        for i in music_i:
            bot.send_audio(message.chat.id, audio=open(f'music/{i}', 'rb'))
        bot.send_message(message.chat.id,"Like it ?\nHit the link in info")




    elif message.text == "/info":
        bot.reply_to(message,"Hello ! My name is Dan and here is my inst - https://www.instagram.com/master_sniffer/ \nGitHub - https://github.com/Master-sniffer \n See ya' later !")
    elif message.text == "/meme":
        bot.send_message(message.chat.id , "Catch your meme !")
        url = 'https://api.imgflip.com/get_memes'
        response = requests.get(url)
        d=response.json()
        data=d['data']['memes']
        pics=[]
        for i in data:
            print (i['url'])
            pics.append(i['url'])

        i=random.choice(pics)
        response = requests.get(i)

        file = open("sample_image.jpg", "wb")
        file.write(response.content)
        file.close()
        photo = open('sample_image.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)



@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):

    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/music')
    itembtnv = types.KeyboardButton('/meme')
    itembtnz = types.KeyboardButton('/info')
    #itembtnc = types.KeyboardButton('c')
    #itembtnd = types.KeyboardButton('d')
    #itembtne = types.KeyboardButton('e')
    markup.row(itembtna, itembtnv , itembtnz)
    #markup.row(itembtnc, itembtnd, itembtne)
    bot.send_message(message.chat.id,"Choose what you want to do !", reply_markup=markup)

    with open ("saves.json" ) as f: #Открытие файла  
        info=json.load(f)
        print ("opening data...") #Лоигрование, что запись в файл идет
    print (info)

    reply=str(random.randint(0,100))
    if 'alexa' in message.text:
        bot.reply_to(message,str("Pishov Nahui"))
        return 
    if str (message.from_user.id) in info:
        reply+=f" {message.from_user.first_name} thats your new number" 
    else:
        with open ("saves.json", "w") as f:
            print ("saving data...")
            data= str(info) + str(message.from_user.id)+","
            json.dump (data, f)
            print (data)
    bot.reply_to(message,reply)


@bot.message_handler(content_types=["sticker"])
def stickos (message:Message):
    bot.send_sticker(message.chat.id, STICKER_ID)
    print (message)

# @bot.inline_handler(lambda query: query.query == 'text')
# def query_text(inline_query):
#     print (inline_query)
#     try:
#         r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
#         r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
#         bot.answer_inline_query(inline_query.id, [r, r2])
#     except Exception as e:
#         print(e)


bot.polling(timeout=60)
