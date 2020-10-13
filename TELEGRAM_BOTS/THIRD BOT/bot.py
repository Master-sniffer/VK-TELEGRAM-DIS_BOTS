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

TOKEN = '1316987589:AAHBZrFcJ4Lt6Zwvt1ObVJeEK7XKBdNI4yE' 

fap="tut_rabota/logs.json"
other_faps=["kvad.jpg","trug.jpg","krug.png","priamoug.jpg","spiral"]

bot=telebot.TeleBot(TOKEN) 

#КОРОЧЕ, ЕПТА
# СНАЧАЛА У НАС ИДУТ КЕЙСЫ, ТИПА ТАСК 0 - ИДЕТ НАХУЙ, А ТАСК 1 ИДЕТ В ЖОПУ
#
#
#


#@bot.edited_message_handler(content_types=["text"])
#@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
@bot.message_handler(commands=['start'])
def Welcome_Message(message):
    spisok=[]
    bot.send_message(message.chat.id, "Привет ! Сегодня мы будем решать кто ты по жизни !\n")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Квадрат', 'Треугольник', "Круг", "Спираль", "Прямоугольник")
    msg = bot.send_message(message.chat.id, "Выберите, пожалуйста, фигуру, глядя на которую вы могли сказать это – я" , reply_markup=markup)
    # Добавить сюда вывод медиа файлов
    bot.register_next_step_handler(msg, task_0 , spisok)




def task_0(message, spisok): 
    spisok.append(message.text)
    times=0
    print (spisok)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    if spisok[0] == "Квадрат":
        markup.add('Треугольник', "Круг", "Спираль", "Прямоугольник")
    
    elif spisok[0]=="Треугольник":
        markup.add('Квадрат', "Круг", "Спираль", "Прямоугольник")
    
    elif spisok[0]=="Круг":
        markup.add('Квадрат', 'Треугольник', "Спираль", "Прямоугольник")
    
    elif spisok[0]=="Спираль":
        markup.add('Квадрат', 'Треугольник', "Круг", "Прямоугольник")

    elif spisok[0]=="Прямоугольник":
        markup.add('Квадрат', 'Треугольник', "Круг", "Спираль")

    msg = bot.reply_to(message, "2. которая наиболее Вам подходит во вторую очередь." ,  reply_markup=markup)
    # Добавить сюда вывод медиа файлов
    
    bot.register_next_step_handler(msg, task_1 , spisok, times)

def task_1(message, spisok, times):
    spisok.append(message.text)
    times+=1
    print (times)
    print (spisok)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Да', 'Нет')

    if times == 1:
        msg = bot.send_message(message.chat.id, "У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times)
    
    elif times==2:
        msg = bot.send_message(message.chat.id, "Профессиональный рост я вижу в обязательном управлении коллективом или проектом." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==3:
        msg = bot.send_message(message.chat.id, "Я быстро разбираюсь в материале с большим количеством деталей и нюансов." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==4:
        msg = bot.send_message(message.chat.id, "Наличие четкого распорядка дня в выбираемой профессии для меня обязательно." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==5:
        msg = bot.send_message(message.chat.id, "Я иногда пишу (писал) стихи" , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==6:
        msg = bot.send_message(message.chat.id, "Я быстро ориентируюсь в незнакомой местности" , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==7:
        msg = bot.send_message(message.chat.id, "Я очень хочу работать в зарубежной компании, работа за границей приоритетна для меня" , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==8:
        msg = bot.send_message(message.chat.id, "Я самостоятельно планирую свои путешествия." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==9:
        msg = bot.send_message(message.chat.id, "Постоянный контакт с людьми в выбираемой профессии для меня очень важен." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==10:
        msg = bot.send_message(message.chat.id, " В профессиональной деятельности, я без труда буду использовать язык символов, графиков и схем." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==11:
        msg = bot.send_message(message.chat.id, "Для меня важно работать в большой организации, где можно подняться по карьерной лестнице." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==12:
        msg = bot.send_message(message.chat.id, "Работа с большим количеством цифровых данных будет интересна для меня." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==13:
        msg = bot.send_message(message.chat.id, "Я хочу, чтобы профессия была связана с созданием чего-то нового." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==14:
        msg = bot.send_message(message.chat.id, "Мне нравится осуществлять контроль и проверку чужой деятельности." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==15:
        msg = bot.send_message(message.chat.id, "Я хочу, чтобы моя профессия была связана с международным партнерством." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==16:
        msg = bot.send_message(message.chat.id, "Я хочу заниматься собственным бизнесом и смогу самостоятельно им управлять." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==17:
        msg = bot.send_message(message.chat.id, "Знакомые часто обращаются ко мне за советом или рекомендацией." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==18:
        msg = bot.send_message(message.chat.id, "Я хорошо планирую и создаю оптимальный маршруты или схемы для решения вопросов." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==19:
        msg = bot.send_message(message.chat.id, "Я слежу за процессами происходящими в обществе и политике, хочу иметь в данной области профессиональную компетенцию." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==20:
        msg = bot.send_message(message.chat.id, "Я быстро адаптируюсь в новых условиях, быстро нахожу контакт с новыми людьми." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times) 

    elif times==21:
        msg = bot.send_message(message.chat.id, "Я часто использую сокращения, мне так проще фиксировать и сохранять информацию." , reply_markup=markup)
        bot.register_next_step_handler(msg, task_1 , spisok, times)
    


    else:
        bot.send_message(message.chat.id, "Пора узнать твои результаты !")
        da="Да"

        if (spisok[0] == "Треугольник" and spisok[1] == "Квадрат") and ((spisok[2]==da and spisok[4]==da and spisok[8]==da and spisok[12]==da and spisok[17]==da  ) or (spisok[4]==da and spisok[12]==da and spisok[13]==da and spisok[16]==da and spisok[18]==da)):
            bot.send_message(message.chat.id, "1")
            loging (message, spisok)
        
        #

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[7]==da and spisok[15]==da and spisok[18]==da   :
            bot.send_message(message.chat.id, "2")
            loging (message, spisok)

        elif (spisok[0] == "Квадрат" and spisok[1] == "Круг") and spisok[5]==da and spisok[11]==da and spisok[13]==da and spisok[14]==da and spisok[22]==da   :
            bot.send_message(message.chat.id, "2")
            loging (message, spisok)
        
        #

        elif (spisok[0] == "Треугольник" and spisok[1] == "Квадрат") and spisok[3]==da and spisok[5]==da and spisok[12]==da and spisok[13]==da and spisok[15]==da   :
            bot.send_message(message.chat.id, "3")
            loging (message, spisok)
        
        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[3]==da and spisok[6]==da and spisok[10]==da and spisok[15]==da and spisok[17]==da   :
            bot.send_message(message.chat.id, "3")
            loging (message, spisok)
        
        #

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[13]==da and spisok[15]==da and spisok[20]==da   :
            bot.send_message(message.chat.id, "4")
            loging (message, spisok)
        
        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[11]==da and spisok[13]==da and spisok[15]==da   :
            bot.send_message(message.chat.id, "4")
            loging (message, spisok)
        
        #

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[12]==da and spisok[13]==da and spisok[15]==da   :
            bot.send_message(message.chat.id, "5")
            loging (message, spisok)
        
        elif (spisok[0] == "Треугольник" and spisok[1] == "Квадрат") and spisok[4]==da and spisok[7]==da and spisok[17]==da and spisok[18]==da and spisok[21]==da   :
            bot.send_message(message.chat.id, "5")
            loging (message, spisok)
        
        #

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[4]==da and spisok[5]==da and spisok[7]==da and spisok[16]==da and spisok[19]==da   :
            bot.send_message(message.chat.id, "6")
            loging (message, spisok)

        elif (spisok[0] == "Квадрат" and spisok[1] == "Треугольник") and spisok[4]==da and spisok[5]==da and spisok[12]==da and spisok[13]==da and spisok[20]==da   :
            bot.send_message(message.chat.id, "6")
            loging (message, spisok)

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[3]==da and spisok[9]==da and spisok[10]==da and spisok[16]==da and spisok[20]==da   :
            bot.send_message(message.chat.id, "6")
            loging (message, spisok)

        #

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[6]==da and spisok[10]==da and spisok[18]==da and spisok[20]==da and spisok[21]==da   :
            bot.send_message(message.chat.id, "7")
            loging (message, spisok)
        
        #

        elif (spisok[0] == "Треугольник" and spisok[1] == "Круг") and spisok[3]==da and spisok[10]==da and spisok[18]==da and spisok[20]==da and spisok[21]==da   :
            bot.send_message(message.chat.id, "8")
            loging (message, spisok)
            

        else :
            bot.send_message(message.chat.id, "HM, SOMETHING WENT WRONG. Try typing /start and complete the whole test again")
            loging (message, spisok)
        



#ИДЕТ ЛОГИРОВАНИЕ
def loging (message, spisok):
    ID= str(message.from_user.id)
    with open (fap, "r") as f:
        firs=json.load(f)
    
    if ID in firs:
        firs[ID]["answers"]=spisok
    
    else :
        firs[ID]={"task":0, "answers":spisok}
    
    with open (fap, "w") as f:
        json.dump(firs,f)



        

"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)
