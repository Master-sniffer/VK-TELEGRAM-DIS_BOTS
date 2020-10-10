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
other_faps=["kvad.jpg","trug.jpg","krug.png","priamoug.jpg","spiral"]

bot=telebot.TeleBot(TOKEN) 

#КОРОЧЕ, ЕПТА
# СНАЧАЛА У НАС ИДУТ КЕЙСЫ, ТИПА ТАСК 0 - ИДЕТ НАХУЙ, А ТАСК 1 ИДЕТ В ЖОПУ
#
#
#


@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"]) #Бот ждет сообщение и если происходит событие - текст, он выполняет функцию
def echo_digits(message:Message):

    def task_0(message):
        pass

    def task_1(message):
        pass
    
    def task_2 (message):
        answer.append(message.text)

    def task_3 (message):
        answer.append(message.text)

    def task_4 (message):
        answer.append(message.text)

    def task_5 (message):
        answer.append(message.text)

    def task_6 (message):
        answer.append(message.text)

    def task_7 (message):
        answer.append(message.text)

    def task_8 (message):
        answer.append(message.text)

    def task_9 (message):
        answer.append(message.text)

    def task_10 (message):
        answer.append(message.text)

    def task_11 (message):
        answer.append(message.text)

    def task_12 (message):
        answer.append(message.text)

    def task_13 (message):
        answer.append(message.text)


    def test(task):
        if task==0:
            msg= bot.send_message (message.chat.id, "1. глядя на которую вы могли сказать это – я")
            bot.register_next_step_handler(msg,task_0)
            task+=1
            test(task)
        
        elif task==1:
            msg = bot.reply_to(message, "2. которая наиболее Вам подходит во вторую очередь.")
            bot.register_next_step_handler(msg,task_1)
            task+=1
            test(task)
        
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
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==4:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==5:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==6:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==7:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==8:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==9:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==10:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==11:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==12:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==13:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==14:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==15:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==16:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==17:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==18:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==19:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==20:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==21:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)

        elif task==22:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, " У меня свободное владения иностранным языком,и я готов (а) проходить на нем обучение.", reply_markup=markup)

            bot.register_next_step_handler(msg, task_2)
            task+=1
            test(task)
        





    ID= str(message.from_user.id) # ID пользователя 

    if message.from_user:
        with open (fap, "r") as f:
            firs=json.load(f)

        if ID in firs:
            pass # думаю здесь ничего не надо вкючать
        else:
            with open (fap, "w") as f:
                firs[ID]["task"]=0
                firs[ID]["answers"]=[]
                json.dump(firs,f)
        
        task=firs[ID]["task"] # нужен для номера задания
        answer=firs[ID]["answers"]

        if task==24:
            pass
        else:
            test(task)
        
        
        
        
        
        

    





"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)
