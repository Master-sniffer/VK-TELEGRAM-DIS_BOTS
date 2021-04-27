# -*- coding: utf-8 -*-
import requests

import sys
import os


#ORM
from sqlalchemy import MetaData, Table, Column, String, Integer, BigInteger, engine, create_engine , Sequence
import sqlalchemy
from sqlalchemy.orm import Session, session, defaultload
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true


#telebot
import telebot

from telebot.types import Message
from telebot import types


TOKEN = '' 
bot=telebot.TeleBot(TOKEN) 



Base = declarative_base() #нужно для ORM для БД

class Database():
    engine=sqlalchemy.create_engine('sqlite:///base_0.db') #Created an engine
    
    def __init__(self):
        self.connection = self.engine.connect() #Created a connection
        print("DB Instance created")
    
    def save_info(self,listes):
        meta=MetaData()
        session=Session(bind=self.connection)
        
        user=base_0( question_0 =str(listes[0]),question_1=str(listes[1]) , question_2=str(listes[2]) , question_3=str(listes[3]), question_4=str(listes[4]) , question_5=str(listes[5]) , question_6=str(listes[6]) , question_7=str(listes[7]), question_8=str(listes[8])    )
        session.merge(user)
        session.commit()


#database
class base_0(Base):
    __tablename__ = 'base_0'
    rowid = Column(Integer, primary_key=true)
    question_0 = Column(String)
    question_1 = Column(String)
    question_2 = Column(String)
    question_3 = Column(String)
    question_4 = Column(String)
    question_5 = Column(String)
    question_6 = Column(String)
    question_7 = Column(String)
    question_8 = Column(String)

    def __repr__(self):
        return "<base_0(question_0='%s', question_1='%s', question_2='%s' , question_3='%s' , question_4='%s' , question_5='%s' , question_6='%s' , question_7='%s' , question_8='%s' )>" % (
                                self.question_0, self.question_1, self.question_2, self.question_3, self.question_4 , self.question_5 , self.question_6 , self.question_7, self.question_8)




class route_1:
    def reply(self , message:Message): #msg
        markup = types.ReplyKeyboardMarkup()
        itembtnv = types.KeyboardButton('/help')
        itembtna = types.KeyboardButton('/1')
        itembtnb = types.KeyboardButton('/2')
        itembtnc = types.KeyboardButton('/3')
        itembtnd = types.KeyboardButton('/4')
        itembtne = types.KeyboardButton('/5')
        markup.row(itembtna,itembtnb,itembtnc,itembtnd,itembtne, itembtnv)
        bot.send_message(message.chat.id, "1) Правовая База стартапа\n2)Успешные истории стартапов\n3)Теоретические аспекты\n4)Актуальные новости и статистика стартапов\n5)Перспективные отрасли", reply_markup=markup)
    
    @bot.message_handler(commands=['1']) # /1
    def message_1(message):
        print("текст")
        bot.send_message(message.chat.id, "текст")

    
    @bot.message_handler(commands=['2']) # /2
    def message_2(message):
        print("текст")
        bot.send_message(message.chat.id, "текст")

    @bot.message_handler(commands=['3']) # /3
    def message3(message):
        print("текст")
        bot.send_message(message.chat.id, "текст")

    @bot.message_handler(commands=['4']) # /4
    def message4(message):
        print("текст")
        bot.send_message(message.chat.id, "текст")

    @bot.message_handler(commands=['5']) # /5
    def message5(message):
        print("текст")
        bot.send_message(message.chat.id, "текст")

route1=route_1()


class route_2:
    def question_0(self, spisok, message):
        msg = bot.send_message(message.chat.id ,"Согласны ли вы с обработкой данных?")
        bot.register_next_step_handler(msg , self.question_1, spisok  )
    
    def question_1(self, message, spisok):
        spisok.append(message.text)
        msg = bot.send_message(message.chat.id ,"Укажите отрасль ?")
        bot.register_next_step_handler(msg, self.question_2 , spisok )

    def question_2(self, message, spisok):
        spisok.append(message.text)
        msg = bot.send_message(message.chat.id ,"Какую проблему вы решаете ?")
        bot.register_next_step_handler(msg, self.question_3 , spisok )

    def question_3(self, message, spisok):
        spisok.append(message.text)
        msg =bot.send_message(message.chat.id ,"Стадия разработки вашего стартапа ?")
        bot.register_next_step_handler(msg, self.question_4  , spisok )

    def question_4(self, message, spisok):
        spisok.append(message.text)
        msg =bot.send_message(message.chat.id ,"Какая правовая форма вашего стартапа?")
        bot.register_next_step_handler(msg, self.question_5  , spisok )

    def question_5(self, message, spisok):
        spisok.append(message.text)
        msg =bot.send_message(message.chat.id ,"Количество вовлечённых участников в стартап ?")
        bot.register_next_step_handler(msg, self.question_6 , spisok)

    def question_6(self, message, spisok):
        spisok.append(message.text)
        msg =bot.send_message(message.chat.id ,"Ваша целевая аудитория ?")
        bot.register_next_step_handler(msg, self.question_7  , spisok)

    def question_7(self, message, spisok):
        spisok.append(message.text)
        msg =bot.send_message(message.chat.id ,"Чего вы хотели долбится ?")
        bot.register_next_step_handler(msg, self.question_8 , spisok )

    def question_8(self, message, spisok):
        spisok.append(message.text)
        msg =bot.send_message(message.chat.id ,"Как вы видите реализацию стартапа ?")
        bot.register_next_step_handler(msg, self.question_End , spisok)

    def question_End( self,message, spisok):
        markup = types.ReplyKeyboardMarkup()
        itembtnv = types.KeyboardButton('/help')
        itembtna = types.KeyboardButton('/start')
        markup.row(itembtna, itembtnv)
        spisok.append(message.text)
        bot.send_message(message.chat.id, "Благодарим вас за потраченное время\nЧтобы вернуться на главную страницу, нажмите start",reply_markup=markup)
        database=Database()
        database.save_info(spisok)

route2=route_2()

@bot.message_handler(commands=['start']) # /start
def Welcome_Message(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Узнать все о стартапе', 'Хочу развивать стартап')

    msg = bot.send_message(message.chat.id, "Что нужно для развития стартапа ?" , reply_markup=markup)
    # Вывод файлов
    bot.register_next_step_handler(msg, raspred )


def raspred(message):
    if (message.text=="Узнать все о стартапе"):
        route1.reply(message)
    
    elif (message.text=="Хочу развивать стартап"):
        spisok=[]
        route2.question_0(spisok,message)





@bot.message_handler(commands=['help']) # /help
def sos(message):
    bot.send_message(message.chat.id, "тут помощь, но какая...")


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
