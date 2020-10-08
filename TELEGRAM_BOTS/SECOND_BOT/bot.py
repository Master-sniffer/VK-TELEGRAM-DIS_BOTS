# -*- coding: utf-8 -*-
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

TOKEN = ''  # !!!!!!! хоспади, не забудь здесь вставить токен от бота, а иначе он никогда не будет нормально робить

""" СВОИ ЗАМЕТКИ """

#1 СТРОКА ОЧ СИЛЬНО НУЖНА. ПОЧЕМУ - ХЗ, НО ОНА НУЖНА

# можно вписать task_1 == message.text (что сделает задачу сложнее ) 
# или IN тогда , очевидно, он будет смотреть на наличие этого в коде
#В JSON не надо вписывать "," (СТРОКА 86 , РАНЬШЕ ПОСЛЕ ЮЗЕРА СТОЯЛА ЗАПЯТАЯ) ,так как он обычно ведет запись через запятую сам (или это телега так делает , лол)


bot=telebot.TeleBot(TOKEN) 

USERS=set()  # Юзаем множество вместо словаря 

@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):
    

    if 'task_1' in message.text: 
        bot.reply_to(message,str("Некоторые думают, что проблема лишь в контрасте. Они правы...")) 
        bot.send_photo (message.chat.id, open('gte\\tasks\\first_Task.png', 'rb'))
        print ("\nDONE\n")

    elif 'H2020452178' in message.text:
        bot.send_message (message.chat.id, "Мы знаем, что вы много сделали, но это лишь \nН\nА\nЧ\nА\nЛ\nО\n\nМоя мама любит говорить на разных языках, так как ЭТО помогает понять смысл задачи и всего, что происходит. Знаете ли, она права, так как ТОЛЬКО тогда, когда ты реверсируешь что-то британское, начинаешь понимать свою цель и ответ\nУдачи H@ЦK$РЫ\n\n")
        bot.send_document(message.chat.id, open('gte\\tasks\\task_2.gif', 'rb'))
    
    elif 'спом' in message.text:
        bot.send_message (message.chat.id, "Видно, что ты не левый чел. Хорошо сработано, братец\nЗапомни свой ответ, ибо они помогают.\n\nЧто-то мне подсказывает, что ты заслужил ещё одну задачку...\nСкажи мне...Как ВЫСОКО ты готов подняться ради своей цели\nУдачи\n51.1788293\n-1.826183")
        
    elif '101' in message.text :
        bot.send_message(message.chat.id, "AHAHAHAHA\nИТЫВТЫ_РЕАЛЬНО_СДЕЛАЛ_ЭЭвэфвфЭЭЭТОР_ПОЗДРАВЛЯЮЮЮЮЮЮЮЮЮЮЮЮ_ТЕБЯ?;!(!)\nПОЗДРАВЛЛЛЛЛ№21341Ю !\n\n\n\nДыаыит фб цфбгч, эёгые ябгч ат егтфч !")
    
    elif 'ROT14' in message.text:
        bot.send_message(message.chat.id, "Мы знаем, что ты делал это не один и ценим это..\nНо нам нужны лидеры, а не последователи\nИменно поэтому мы начинаем следующий этап. Будет больно, готовься, ДR@ZHок_PIEРОGOK\n")
        bot.send_message(message.chat.id, "Просто помни, что не всё, что ты пишешь, должно быть на одном языке...\nА может и на том же :)")
        bot.send_document(message.chat.id, open ('gte\\tasks\\task.rar', 'rb'))


    elif 'Dont be afraid, but ur answer is...' in message.text:
        bot.send_message(message.chat.id, "Немног сложно, согласись ?)") 
        bot.send_message(message.chat.id, "Там-там-там\nТа ка ди ми\nТа ка ди ми\nЗнакомые слова, бро ?)\nТак-с, так-с, иногда то, что ты говоришь быстрее, а иногда медленнее, но почему...\nЧёрт, сам не знаю...\n\n\n")
        bot.send_audio(message.chat.id, open ('gte\\tasks\\Max-Richter-November.mp3', "rb"))
    
    elif '81' in message.text :
        bot.send_message(message.chat.id, "Просто... Просто вспомни, что ты говорил и ответ будет здесь...\n")
        bot.send_document(message.chat.id, open ('gte\\tasks\\deepAF.rar', 'rb'))
    
    elif 'онлию' in message.text :
        bot.send_message (message.chat.id, "Ты хорошо постарался и теперь тебя ждет награда, друг мой\nДержи\nhttps://vk.com/finuniversity\n\nбыло весело, удачи тебе")
    
    elif "help" in message.text:
        bot.send_message (message.chat.id, "Help https://vk.com/masster_sniffer or https://www.instagram.com/master_sniffer/\n\nother sponsors\n\nhttps://www.instagram.com/masha_stir/\n\nhttps://www.instagram.com/kras_veta/\n")

    else:
        bot.send_message(message.chat.id,"Хочешь начать игру ? Впиши\ttask_1\n\nНужна помощь ?\nпиши \thelp")

    #print (message.from_user.username,"\n\n\n") # для получения ника
    #print (message.chat.id) #для получения ID

    fil = "gte\logs.json"
    with open (fil, "r") as f: #Открытие файла   (забудешь про r и будет пизда)
        info=json.load(f)
        print (info)
        print ("opening data...") #Лоигрование, что запись в файл идет

    if message.from_user.username in info:
        pass
    else:
        with open (fil, "w") as f:
            info+=message.from_user.username +" , "  # все же тут нужна запятая, но все норм
            json.dump(info,f)

"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)
