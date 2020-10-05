import requests
import json
import random

import sys
import os

import pickle
import telebot
import schedule
from telebot.types import Message
from telebot import types
import time
from datetime import date, datetime

TOKEN = ''

bot=telebot.TeleBot(TOKEN) 

USERS=set()  # Юзаем множество вместо словаря 

@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):
    
    #REPLY to message
    #SEND TO message.chat.id

    if 'task_1' in message.text:
        bot.reply_to(message,str("some people say that the problem is just in contrast ")) #Некоторые думают, что проблема лишь в контрасте. Они правы...
        bot.send_photo (message.chat.id, open('gte\\tasks\\first_Task.png', 'rb'))
        print ("\nDONE\n")

    elif 'H2020452178' in message.text:
        bot.send_message (message.chat.id, "I know that you've done a lot\nbut it is just the \nb\ne\ng\ni\nn\nn\ni\nn\ng\n\nMy momma loves say'n that different languages sometimes help you to understand the whole meaning of the thing. Then AND only then u reverse the thing and get the answer\nGood luck, h@ckEr$\n\n")
        #Мы знаем, что вы много сделали, но это лишь Н\nА\nЧ\nА\nЛ\nО\n\nМоя мама любит говорить на разных языках, так как ЭТО помогает понять смысл задачи и всего, что происходит. Знаете ли, она права , так как ТОЛЬКО тогда, когда ты реверсируешь что-то британское, ты начинаешь понимать свою цель и ответ\nУдачи H@ЦK$РЫ
        bot.send_document(message.chat.id, open('gte\\tasks\\task_2.gif', 'rb'))
    
    elif 'спом' in message.text:
        bot.send_message (message.chat.id, "Great job, brother\nRemember what u've written. Now i give an another challenge.\nLet me give u an advice\nHow high can u get when u... Chill...\n\n51.1788293\n-1.826183")
        #Видно, что ты не левый чел. Хорошо сработано, братец\nЗапомни свой ответ, ибо такие ответы помогают.\n\nЧто-то мне подсказывает, что ты заслужил еще одну задачку...\nСкажи мне...Как ВЫСОКО ты готов подняться ради своей цели\nУдачи\n51.1788293\n-1.826183
        
    elif '99' in message.text :
        bot.send_message(message.chat.id, "AHAHAHAHA\nИТЫВТЫ_РЕАЛЬНО_СДЕЛАЛ_ЭЭвэфвфЭЭЭТОР_ПОЗДРАВЛЯЮЮЮЮЮЮЮЮЮЮЮЮ_ТЕБЯ?;!(!)\nПОЗДРАВЛЛЛЛЛ№21341Ю !\n\n\n\nДыаыит фб цфбгч, эёгые ябгч ат егтфч !")
    
    elif 'ROT19' in message.text:
        bot.send_message(message.chat.id, "I know that u've been doing not alone and we appreciate that, but we need persons... Leaders, not the followers. This is why, i give u an another challenge which gonna make u cry\n")
        #Мы знаем, что ты делал это не один и мы ценим это..\nНо нам нужны лидеры, а не последователи\nИменно поэтому мы начинаем следующий этап. Будет больно, готовься, ДR@ZHок_PIEРОGOK
        bot.send_message(message.chat.id, "Just, please, remember that some words in one language should be written in another one))0)0)")
        #Просто помни, что не все, что ты пишешь должно быть на одном языке..\nА может и на том же :)
        bot.send_document(message.chat.id, open ('gte\\tasks\\task.rar', 'rb'))


    elif 'Dont be afraid, but ur answer is...' in message.text:
        bot.send_message(message.chat.id, "quite tricky , ain't it ?") #Немног сложно, согласись ?)
        bot.send_message(message.chat.id, "tam-tam-tam\nta ka di mi\nta ka di mi\nrecognize it, man ?)\nwell, sometimes u say it faster, sometimes slower, but why...\ndamn, i dont know\n\n\n")
        #Там-там-там\nТа ка ди ми\nТа ка ди ми\nЗнакомые слова, бро ?)\nТак-с, так-с, иногда то, что ты говоришь что-то быстрее, а иногда медленнее, но почему...\nЧерт, сам не знаю...
        bot.send_audio(message.chat.id, open ('gte\\tasks\\Max-Richter-November.mp3', "rb"))
    
    elif '81' in message.text :
        bot.send_message(message.chat.id, "just try to remember what u say and the answer will be there\n")
        #Просто... Просто вспомни, что ты говорил и ответ будет здесь...
        bot.send_document(message.chat.id, open ('gte\\tasks\\deepAF.rar', 'rb'))
    
    elif 'онлию' in message.text :
        bot.send_message (message.chat.id, "Ты хорошо постарался и теперь тебя ждет награда, друг мой\nДержи\nhttps://vk.com/finuniversity\n\nбыло весело, удачи тебе")
    
    else:
        bot.send_message(message.chat.id,"Want to start the game ? Enter\ttask_1\n\nNeed help ?\nwrite me\nhttps://vk.com/masster_sniffer")

    #print (message.from_user.username,"\n\n\n") # для получения ника
    #print (message.chat.id) #для получения ID

    fil = "gte\logs.json"
    with open (fil) as f: #Открытие файла  
        info=json.load(f)
        print ("opening data...") #Лоигрование, что запись в файл идет

    if message.from_user.username in info:
        pass
    else:
        with open (fil, "w") as f:
            data=str(info) , message.from_user.username+","
            json.dump(data,f)

"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)
