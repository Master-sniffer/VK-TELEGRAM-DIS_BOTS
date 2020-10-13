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

fap="/Users/NONE/Desktop/VISUAL CODE/Side folder/Telegram bot/Second bot/tut_rabota/logs.json"
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
def echo_digits(message , where_call=None):

    def zapic():
        print (firs)
        with open (fap, "w") as f:
            json.dump(firs,f)


    def task_0(message):
        print(message)
        print (message.text)
        print ("Nice text")
        

    def task_1(message):
        print (task)
    
    def task_2 (message):
        answer.append(message.text)
        print ("we are here")

    def task_23 (message):
        pass



    def test(message ,task):
        if task==0:
            task+=1
            msg= bot.send_message (message.chat.id, "1. глядя на которую вы могли сказать это – я")
            bot.register_next_step_handler(msg,task_0)
            print (task )
            print ("\n\nHERE\n\n")
            zapic()
            #task+=1
            test(message, task)
        
        elif task==1:
            msg = bot.reply_to(message, "2. которая наиболее Вам подходит во вторую очередь.")
            bot.register_next_step_handler(msg,lambda message :task_1(message))
            task+=1
            test(message, task)
        
        elif task==2:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==3:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " Профессиональный рост я вижу в обязательном управлении коллективом или проектом.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==4:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " Я быстро разбираюсь в материале с большим количеством деталей и нюансов.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==5:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Наличие четкого распорядка дня в выбираемой профессии для меня обязательно.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==6:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я иногда пишу (писал) стихи.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==7:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я быстро ориентируюсь в незнакомой местности", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==8:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я очень хочу работать в зарубежной компании, работа за границей приоритетна для меня", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==9:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я самостоятельно планирую свои путешествия.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==10:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Постоянный контакт с людьми в выбираемой профессии для меня очень важен.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==11:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " В профессиональной деятельности, я без труда буду использовать язык символов, графиков и схем. ", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==12:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, ". Для меня важно работать в большой организации, где можно подняться по карьерной лестнице. ", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==13:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Работа с большим количеством цифровых данных будет интересна для меня.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==14:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я хочу, чтобы профессия была связана с созданием чего-то нового.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==15:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Мне нравится осуществлять контроль и проверку чужой деятельности.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==16:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я хочу, чтобы моя профессия была связана с международным партнерством.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==17:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я хочу заниматься собственным бизнесом и смогу самостоятельно им управлять. ", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==18:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " Знакомые часто обращаются ко мне за советом или рекомендацией.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==19:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я хорошо планирую и создаю оптимальный маршруты или схемы для решения вопросов.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==20:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я слежу за процессами происходящими в обществе и политике, хочу иметь в данной области профессиональную компетенцию.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==21:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я быстро адаптируюсь в новых условиях, быстро нахожу контакт с новыми людьми. ", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==22:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, "Я часто использую сокращения, мне так проще фиксировать и сохранять информацию.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)
        

        elif task==23:
            msg = bot.send_message(message.chat.id, "Давай узнаем твои результаты")
            bot.register_next_step_handler(msg, task_23)

        else :
            bot.send_message(message.chat.id, "sorry snake")





    ID= str(message.from_user.id) # ID пользователя 

    if message.from_user:
        with open (fap, "r") as f:
            firs=json.load(f)

        if ID in firs:
            pass

        else:
            with open (fap, "w") as f:
                firs[ID]={"task":0, "answers":[]}
                print (firs)
                json.dump(firs,f)
        
        task=firs[ID]["task"] # нужен для номера задания
        answer=firs[ID]["answers"]

        if task==23:
            pass
        else:
            print ("\n\nWTF\n\n")
            test(message,task)
        

"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)
