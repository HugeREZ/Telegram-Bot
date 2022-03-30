# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import schedule
import sps_script
import telebot
import gc

token = "?"
bot = telebot.TeleBot(token)
chat_id = '?'#ввести id необходимого чата



#print(time.ctime())


schedule.every(2).days.at("08:00").do(sps_script.utro)
schedule.every().day.at("12:00").do(sps_script.dnevnoy)
schedule.every().day.at("16:00").do(sps_script.vecher)



"""
#ниже для проверки
schedule.every(1).minutes.do(sps_script.utro)
#schedule.every(1).minutes.do(sps_script.dnevnoy)
#schedule.every(1).minutes.do(sps_script.vecher) 
"""
while 1:
    gc.collect()
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    bot.polling(none_stop=True)