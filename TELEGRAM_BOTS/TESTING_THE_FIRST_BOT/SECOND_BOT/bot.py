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
        bot.reply_to(message,str("some people say that the problem is just in contrast "))  
        bot.send_photo (message.chat.id, "first_Task.png")

    elif 'H2020452178' in message.text:
        bot.send_message (message.chat.id, "I know that you've done a lot\nbut it is just the \nb\ne\ng\ni\nn\nn\ni\nn\ng\n\nMy momma loves say'n that different languages sometimes help you to understand the whole meaning of the thing. Then AND only then u reverse the thing and get the answer\nGood luck, h@ckEr$\n\n")
        bot.send_document(message.chat.id, "task_2.gif")
    
    elif 'спом' in message.text:
        bot.send_message (message.chat.id, "Great job, brother\nRemember what u've written. Now i give an another challenge.\nLet me give u an advice\nHow high can u get when u... Chill...\n\n51.1788293\n-1.826183")
    
    elif '99' in message.text :
        bot.send_message(message.chat.id, "AHAHAHAHA\n U've REALlaadlaLY DADANDANDONE IT\nCONGRATS !\n\n\n\nДыаыит фб цфбгч, эёгые ябгч ат егтфч !")
    
    elif 'ROT19' in message.text:
        bot.send_message(message.chat.id, "I know that u've been doing not alone and we appreciate that, but we need persons... Leaders, not the followers. This is why, i give u an another challenge which gonna make u cry\n")
        bot.send_message(message.chat.id, "Just, please, remember that some words in one language should be written in another one))0)0)")
        bot.send_document(message.chat.id, "task.rar")


    elif 'Dont be afraid, but ur answer is...' in message.text:
        bot.send_message(message.chat.id, "quite tricky , ain't it ?")
        bot.send_message(message.chat.id, "tam-tam-tam\nta ka di mi\nta ka di mi\nrecognize it, man ?)\nwell, sometimes u say it faster, sometimes slower, but why...\ndamn, i dont know\n\n\n")
        bot.send_audio(message.chat.id, "Max-Richter-November.mp3")
    
    elif '81' in message.text :
        bot.send_message(message.chat.id, "just try to remember what u say and the answer will be there\n")
        bot.send_document(message.chat.id, "deepAF.rar")
    
    elif 'онлию' in message.text :
        bot.send_message (message.chat.id, "Ты хорошо постарался и теперь тебя ждет награда, друг мой\nДержи\nhttps://vk.com/finuniversity\n\nбыло весело, удачи тебе")
    
    else:
        bot.send_message(message.chat.id,"Want to start the game ? Enter\ttask_1\n\nneed help ?\nwrite me\nhttps://vk.com/masster_sniffer")

    

"""ЗДЕСЬ РАСПОЛОЖЕНА ПАНЕЛЬ УПРАВЛЕНИЯ ЗАПУСКОМ БОТА """
#ОТВЕЧАЕТ ЗА ЗАПУСК 
bot.polling(none_stop=True)
