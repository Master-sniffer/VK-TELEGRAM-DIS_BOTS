import requests
import json
import random
import pickle
import telebot
from telebot.types import Message
from telebot import types

TOKEN = '1379710116:AAG9BmigUQlgZKnQ3_JEWqKo--7HbbiF1O0'
STICKER_ID=['CAACAgIAAxkBAAIE9V9LoyCFM93_q7nZN72rVKPBgq2bAAKgAANrCxQU3fjzlwNRf_gbBA','CAACAgIAAxkBAAIE7V9LonfNKQgaGLRhRGbspoJMZG5nAAK9AANrCxQUKiCIDDep1_cbBA'] # найдите стикос по души и отправляйте его :)

bot=telebot.TeleBot(TOKEN)

USERS=set()  # Юзаем множество вместо словаря 


@bot.message_handler(commands=["music",'meme_template', "random_meme",'random_doggo','info'])
def commands_and_handler(message:Message):
    if message.text == "/music":
        bot.reply_to(message, "Hey, bro, listen to my music\nYou'll see now a random track")
        music_i=["Heshi.mp3","bass-drive.mp3",'wait.mp3','is it you.mp3','The world which you cannot change.mp3','psy_1.mp3','Bass drive_1.mp3','silence.mp3']
        i=random.choice(music_i)
        bot.send_audio(message.chat.id, audio=open(f'music/{i}', 'rb'))
        bot.send_message(message.chat.id,"Like it ?\nHit the link in info")


    elif message.text == "/info":
        bot.reply_to(message,"Hello ! My name is Dan and here is my inst - https://www.instagram.com/master_sniffer/ \nGitHub - https://github.com/Master-sniffer \n See ya' later !")
    elif message.text == "/meme_template":
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

    elif message.text=="/random_meme":
        bot.send_message(message.chat.id, "Eo, brother. Catch one random meme !\n")
        r=requests.get('https://some-random-api.ml/meme')
        rok=r.json()
        pica=rok['image']
        response = requests.get(pica)

        file = open("random_image.jpg", "wb")
        file.write(response.content)
        file.close()
        photo = open('random_image.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    
    elif message.text=="/random_doggo":
        bot.send_message(message.chat.id, "Hey, hon. Catch pup !\n")
        r=requests.get('https://dog.ceo/api/breeds/image/random')
        rok=r.json()
        print (r)
        pica=rok['message']
        response = requests.get(pica)

        file = open("random_doggo.jpg", "wb")
        file.write(response.content)
        file.close()
        photo = open('random_doggo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)




@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):

    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/music')
    itembtnv = types.KeyboardButton('/meme_template')
    itembtnk = types.KeyboardButton('/random_meme')
    itembtng = types.KeyboardButton('/random_doggo')    
    itembtnz = types.KeyboardButton('/info')
    #itembtnc = types.KeyboardButton('c')
    #itembtnd = types.KeyboardButton('d')
    #itembtne = types.KeyboardButton('e')
    markup.row(itembtna, itembtnv )
    markup.row(itembtnk,itembtng )
    markup.row(itembtnz)
    bot.send_message(message.chat.id,"Choose what you want to do !\nThere are some squares on the bottom of the screen. Use the, to navigate\n\nIf you write something, bot will reply to u with a random number", reply_markup=markup)

    with open ("saves.json" ) as f: #Открытие файла  
        info=json.load(f)
        print ("opening data...") #Лоигрование, что запись в файл идет
    print (info)

    reply=str(random.randint(0,100))
    # if 'alexa' in message.text:
    #     bot.reply_to(message,str("Pishov Nahui"))
    #     return 
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
    stic=random.choice(STICKER_ID)
    bot.send_sticker(message.chat.id, stic)
    print (message)
    print ("\n\n\nHELLO\n\n\n")
    sticka = message.json['sticker']['file_id']
    with open ('sticks.json') as f:
        data=json.load(f)
        if str(sticka)+',' in data:
            print ("\n\nSticka is there already\n\n")
            pass
        else:
            print ("\n\nSticka is being saved\n\n")
            with open ('sticks.json','w') as fa:
                data+=sticka
                data+=","
                json.dump(data, fa)
    stickk=data
    lis=list(stickk)
    data=[]
    nus=len(lis)
    i=0
    word=''
    while i != nus:
        if lis[i]!=',':
            word+=str(lis[i])
        elif lis[i]==",":
            data.append(word)
            word=''
        else:
            word+=lis[i]
        i+=1
    print (data)        
    bot.send_sticker(message.chat.id, random.choice(data))


# bot.polling(timeout=0.1)

"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)