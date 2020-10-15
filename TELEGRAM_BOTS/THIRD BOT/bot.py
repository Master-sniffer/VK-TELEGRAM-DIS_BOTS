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

TOKEN = '' 

fap="tut_rabota/logs.json"
other_faps=["kvad.jpg","trug.jpg","krug.png","priamoug.jpg"]

bot=telebot.TeleBot(TOKEN) 

#КОРОЧЕ, ЕПТА
# СНАЧАЛА У НАС ИДУТ КЕЙСЫ, ТИПА ТАСК 0 - ИДЕТ НАХУЙ, А ТАСК 1 ИДЕТ В ЖОПУ
#
#
#


#@bot.edited_message_handler(content_types=["text"])
#@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
@bot.message_handler(commands=['start']) # /start
def Welcome_Message(message):
    spisok=[]
    bot.send_message(message.chat.id, "Привет ! Сегодня мы будем решать кто ты по жизни !\n")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Квадрат', 'Треугольник', "Круг", "Прямоугольник")

    # photo = open('/tmp/photo.png', 'rb')
    # tb.send_photo(chat_id, photo)



    msg = bot.send_message(message.chat.id, "Выберите, пожалуйста, фигуру, глядя на которую вы могли сказать это – я" , reply_markup=markup)
    # Вывод файлов
    for i in other_faps:
        bot.send_photo(message.chat.id, photo=open(f'tut_rabota/tasks/{i}', 'rb'))
    bot.register_next_step_handler(msg, task_0 , spisok)




def task_0(message, spisok): 
    spisok.append(message.text)
    times=0
    print (spisok)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    if spisok[0] == "Квадрат":
        uno=['trug.jpg', "krug.png", "priamoug.jpg"]  
        markup.add('Треугольник', "Круг", "Прямоугольник")
    
    elif spisok[0]=="Треугольник":
        uno=['kvad.jpg', "krug.png", "priamoug.jpg"]
        markup.add('Квадрат', "Круг", "Прямоугольник")
    
    elif spisok[0]=="Круг":
        uno=['kvad.jpg', 'trug.jpg', "priamoug.jpg"]
        markup.add('Квадрат', 'Треугольник', "Прямоугольник")
    

    elif spisok[0]=="Прямоугольник":
        uno=['kvad.jpg', 'trug.jpg', "krug.png"]
        markup.add('Квадрат', 'Треугольник', "Круг")
    


    msg = bot.reply_to(message, "2. которая наиболее Вам подходит во вторую очередь." ,  reply_markup=markup)

    #Тут идет вывод файлов
    for i in uno:
        bot.send_photo(message.chat.id, photo=open(f'tut_rabota/tasks/{i}', 'rb'))

    bot.register_next_step_handler(msg, task_1 , spisok, times)

    
def task_1(message, spisok, times):
    spisok.append(message.text)
    times+=1
    print (times)
    print (spisok)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Да', 'Нет')

    if times == 1:
        msg = bot.send_message(message.chat.id, "1. У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times)
    
    elif times==2:
        msg = bot.send_message(message.chat.id, "2. Профессиональный рост я вижу в обязательном управлении коллективом или проектом." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==3:
        msg = bot.send_message(message.chat.id, "3. Я быстро разбираюсь в материале с большим количеством деталей и нюансов." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==4:
        msg = bot.send_message(message.chat.id, "4. Наличие четкого распорядка дня в выбираемой профессии для меня обязательно." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==5:
        msg = bot.send_message(message.chat.id, "5. Я иногда пишу (писал) стихи" , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==6:
        msg = bot.send_message(message.chat.id, "6. Я быстро ориентируюсь в незнакомой местности" , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==7:
        msg = bot.send_message(message.chat.id, "7. Я очень хочу работать в зарубежной компании, работа за границей приоритетна для меня" , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==8:
        msg = bot.send_message(message.chat.id, "8. Я самостоятельно планирую свои путешествия." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==9:
        msg = bot.send_message(message.chat.id, "9. Постоянный контакт с людьми в выбираемой профессии для меня очень важен." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==10:
        msg = bot.send_message(message.chat.id, "10. В профессиональной деятельности, я без труда буду использовать язык символов, графиков и схем." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==11:
        msg = bot.send_message(message.chat.id, "11. Для меня важно работать в большой организации, где можно подняться по карьерной лестнице." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==12:
        msg = bot.send_message(message.chat.id, "12. Работа с большим количеством цифровых данных будет интересна для меня." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==13:
        msg = bot.send_message(message.chat.id, "13. Я хочу, чтобы профессия была связана с созданием чего-то нового." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==14:
        msg = bot.send_message(message.chat.id, "14. Мне нравится осуществлять контроль и проверку чужой деятельности." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==15:
        msg = bot.send_message(message.chat.id, "15. Я хочу, чтобы моя профессия была связана с международным партнерством." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==16:
        msg = bot.send_message(message.chat.id, "16. Я хочу заниматься собственным бизнесом и смогу самостоятельно им управлять." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==17:
        msg = bot.send_message(message.chat.id, "17. Знакомые часто обращаются ко мне за советом или рекомендацией." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==18:
        msg = bot.send_message(message.chat.id, "18. Я хорошо планирую и создаю оптимальный маршруты или схемы для решения вопросов." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==19:
        msg = bot.send_message(message.chat.id, "19. Я слежу за процессами происходящими в обществе и политике, хочу иметь в данной области профессиональную компетенцию." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==20:
        msg = bot.send_message(message.chat.id, "20. Я быстро адаптируюсь в новых условиях, быстро нахожу контакт с новыми людьми." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==21:
        msg = bot.send_message(message.chat.id, "21. Я часто использую сокращения, мне так проще фиксировать и сохранять информацию." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times)
    


    else:
        bot.send_message(message.chat.id, "Пора узнать твои результаты !")
        da="Да"

        if (spisok[0] == "Треугольник" and spisok[1] == "Квадрат") and ((spisok[2]==da and spisok[4]==da and spisok[8]==da and spisok[12]==da and spisok[17]==da  ) or (spisok[4]==da and spisok[12]==da and spisok[13]==da and spisok[16]==da and spisok[18]==da)):
            bot.send_message(message.chat.id, "Локация: м. Аэропорт\n\nФакультет: Международных экономических отношений")
            loging (message, spisok)
        
        # 2

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[7]==da and spisok[15]==da and spisok[18]==da   :
            bot.send_message(message.chat.id, "Локация: м. Семеновская\n\nФакультет: Информационных технологий и анализа больших данных")
            loging (message, spisok)

        elif (spisok[0] == "Квадрат" and spisok[1] == "Круг") and spisok[5]==da and spisok[11]==da and spisok[13]==da and spisok[14]==da and spisok[22]==da   :
            bot.send_message(message.chat.id, "Локация: м. Семеновская\n\nФакультет: Информационных технологий и анализа больших данных")
            loging (message, spisok)
        
        # 3

        elif (spisok[0] == "Треугольник" and spisok[1] == "Квадрат") and spisok[3]==da and spisok[5]==da and spisok[12]==da and spisok[13]==da and spisok[15]==da   :
            bot.send_message(message.chat.id, "Локация: м. Динамо\n\nФакультет: «Высшая школа управления»")
            loging (message, spisok)
        
        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[3]==da and spisok[6]==da and spisok[10]==da and spisok[15]==da and spisok[17]==da   :
            bot.send_message(message.chat.id, "Локация: м. Динамо\n\nФакультет: «Высшая школа управления»")
            loging (message, spisok)
        
        # 4

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[13]==da and spisok[15]==da and spisok[20]==da   :
            bot.send_message(message.chat.id, "Локация: м. Динамо\n\nФакультет: Налогов, аудита и бизнес- анализа")
            loging (message, spisok)
        
        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[11]==da and spisok[13]==da and spisok[15]==da   :
            bot.send_message(message.chat.id, "Локация: м. Динамо\n\nФакультет: Налогов, аудита и бизнес- анализа")
            loging (message, spisok)
        
        # 5

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[12]==da and spisok[13]==da and spisok[15]==da   :
            bot.send_message(message.chat.id, "Локация: м. Китай-город\n\nФакультет: Финансовый")
            loging (message, spisok)
        
        elif (spisok[0] == "Треугольник" and spisok[1] == "Квадрат") and spisok[4]==da and spisok[7]==da and spisok[17]==da and spisok[18]==da and spisok[21]==da   :
            bot.send_message(message.chat.id, "Локация: м. Китай-город\n\nФакультет: Финансовый")
            loging (message, spisok)
        
        # 6

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[4]==da and spisok[5]==da and spisok[7]==da and spisok[16]==da and spisok[19]==da   :
            bot.send_message(message.chat.id, "Локация: м. ВДНХ\n\nФакультет: Экономики и бизнеса")
            loging (message, spisok)

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[12]==da and spisok[13]==da and spisok[20]==da   :
            bot.send_message(message.chat.id, "Локация: м. ВДНХ\n\nФакультет: Экономики и бизнеса")
            loging (message, spisok)

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[3]==da and spisok[9]==da and spisok[10]==da and spisok[16]==da and spisok[20]==da   :
            bot.send_message(message.chat.id, "Локация: м. ВДНХ\n\nФакультет: Экономики и бизнеса")
            loging (message, spisok)

        # 7

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[6]==da and spisok[10]==da and spisok[18]==da and spisok[20]==da and spisok[21]==da   :
            bot.send_message(message.chat.id, "Локация: м. Аэропорт\n\nФакультет: Социальных наук и массовых коммуникаций")
            loging (message, spisok)
        
        # 8

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[3]==da and spisok[10]==da and spisok[18]==da and spisok[20]==da and spisok[21]==da   :
            bot.send_message(message.chat.id, "Локация: м. Рязанский пр-т\n\nФакультет: Юридический")
            loging (message, spisok)
            

        else :
            bot.send_message(message.chat.id, "Сразу видно, что ты смышленный малый.\nПопробуй посмотреть все факультеты и реши, какой тебе больше нравится:\nЮридический\nСоциальных наук и массовых коммуникаций\nЭкономики и бизнеса\nФинансовый\nНалогов, аудита и бизнес- анализа\nИнформационных технологий и анализа больших данных\nМеждународных экономических отношений")
            loging (message, spisok)
        



#ИДЕТ ЛОГИРОВАНИЕ
def loging (message, spisok):
    ID= str(message.from_user.id)
    with open (fap, "r") as f:
        firs=json.load(f)
    
    if ID in firs:
        print (spisok)
        print ("alah")
        print(firs)
        firs[ID]={"answers":spisok}
    
    else :
        firs[ID]={"answers":spisok}
    
    with open (fap, "w") as f:
        json.dump(firs,f)


@bot.message_handler(commands=['help']) # /help
def sos(message):
    bot.send_message(message.chat.id, "Нужна помощь - пиши в вк или инст !\nВК - https://vk.com/masster_sniffer \n\nInst - https://www.instagram.com/master_sniffer/")

@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"])
def help(message:Message):
    markup = types.ReplyKeyboardMarkup()
    itembtnv = types.KeyboardButton('/help')
    itembtna = types.KeyboardButton('/start')
    markup.row(itembtna, itembtnv)
    bot.send_message(message.chat.id, "Чтобы начать опрос нажми start\n\nЧтобы получить помощь пишите help", reply_markup=markup)


        

"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)
