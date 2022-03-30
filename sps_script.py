#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import linecache
import re
import argparse
import telebot
import gc


bot = telebot.TeleBot('?')

chat_id = '?'


def utro():
    def count_lines(file):
        try:
            with open('1txt_utro.txt', encoding='utf-8') as fl:
                return len(fl.readlines())
        except Exception:
            return 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    print("Количество строк")
    print(count_lines(args.file))
    perem = count_lines(args.file)

    def zamena():

        if perem == 0:
            with open("1utro_sps.txt", encoding='utf-8') as f:
                with open("1txt_utro.txt", "w", encoding='utf-8') as f1:
                    for line in f:
                        f1.write(line)
            f.close()
            f1.close()

            """# построчное чтение
            
            print('-------')
            with open("1txt_utro.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

            a = 1
            b = count_lines(args.file)
            rnd_numb = random.randint(a, b)
            stroke_by_rnd = ''
            stroke_by_rnd = linecache.getline("1txt_utro.txt", rnd_numb)
            bot.send_message(chat_id, stroke_by_rnd)

            print("Файл обновился")
            #print(stroke_by_rnd)

            with open("1txt_utro.txt", "r+", encoding='utf-8') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != stroke_by_rnd:
                        f.write(i)
                f.truncate()

            gc.collect()
        elif perem == 1:
            """# построчное чтение
            print('-------')
            with open("1txt_utro.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

            #global last_stroke, str
            last_line = 'й'

            with open('1txt_utro.txt', "r", encoding='utf-8') as f1:
                last_line = f1.readlines()[-1]
            print(last_line)


            bot.send_message(chat_id, last_line)

            readFile = open("1txt_utro.txt", encoding='utf-8')
            lines = readFile.readlines()
            readFile.close()
            w = open("1txt_utro.txt", 'w', encoding='utf-8')
            w.writelines([item for item in lines[:-1]])
            w.close()


        elif perem > 1:

            #построчное чтение
            print('-------')
            with open("1txt_utro.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            #end

            a = 1
            b = count_lines(args.file)
            # b = b - 1
            #print(b)
            rnd_numb = random.randint(a, b)

            stroke_by_rnd = 'empty strok'
            print("!!!!!")
            print(stroke_by_rnd)

            stroke_by_rnd = linecache.getline("1txt_utro.txt", rnd_numb)
            bot.send_message(chat_id, stroke_by_rnd)
            print("!!!!!")
            print(stroke_by_rnd)

            with open('1txt_utro.txt', encoding='utf-8') as f:
                lines = f.readlines()
                lines[rnd_numb - 1] = ''  # <- or whatever kind of newline is relevant for your system
            with open('1txt_utro.txt', 'w', encoding='utf-8') as f:
                f.writelines(lines)

            pattern = re.compile(re.escape(stroke_by_rnd))
            with open('1txt_utro.txt', 'w', encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)


            #f.close()

            """# построчное чтение
            print('-------')
            with open("1txt_utro.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""


        else:
            print('Nothing')


    zamena()
    gc.collect()


def dnevnoy():
    def count_lines(file):
        try:
            with open('2txt_dnevnoy.txt', encoding='utf-8') as fl:
                return len(fl.readlines())
        except Exception:
            return 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    perem = count_lines(args.file)

    def zamena2():

        if perem == 0:

            with open("2dnevnoy_sps.txt", encoding='utf-8') as f:
                with open("2txt_dnevnoy.txt", "w", encoding='utf-8') as f1:
                    for line in f:
                        f1.write(line)
            f.close()
            f1.close()

            """# построчное чтение
            print('-------')
            with open("2txt_dnevnoy.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

            a = 1
            b = count_lines(args.file)
            rnd_numb = random.randint(a, b)

            stroke_by_rnd = ''
            stroke_by_rnd = linecache.getline("2txt_dnevnoy.txt", rnd_numb)
            bot.send_message(chat_id, stroke_by_rnd)



            with open("2txt_dnevnoy.txt", "r+", encoding='utf-8') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != stroke_by_rnd:
                        f.write(i)
                f.truncate()

            gc.collect()
        elif perem == 1:
            """# построчное чтение
            print('-------')
            with open("2txt_dnevnoy.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

            #global last_stroke, str
            last_line = 'й'

            with open('2txt_dnevnoy.txt', "r", encoding='utf-8') as f1:
                last_line = f1.readlines()[-1]
            #print(last_line)

            """last_stroke = linecache.getline('1txt_utro.txt', 1)
            print('Последняя строка')
            print(last_stroke)"""

            bot.send_message(chat_id, last_line)

            readFile = open("2txt_dnevnoy.txt", encoding='utf-8')
            lines = readFile.readlines()
            readFile.close()
            w = open("2txt_dnevnoy.txt", 'w', encoding='utf-8')
            w.writelines([item for item in lines[:-1]])
            w.close()

        elif perem > 1:

            """#построчное чтение
            print('-------')
            with open("2txt_dnevnoy.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            #end"""

            a = 1
            b = count_lines(args.file)
            # b = b - 1
            #print(b)
            rnd_numb = random.randint(a, b)


            stroke_by_rnd = 'й'
            stroke_by_rnd = linecache.getline("2txt_dnevnoy.txt", rnd_numb)
            bot.send_message(chat_id, stroke_by_rnd)

            with open('2txt_dnevnoy.txt', encoding='utf-8') as f:
                lines = f.readlines()
                lines[rnd_numb - 1] = ''  # <- or whatever kind of newline is relevant for your system
            with open('2txt_dnevnoy.txt', 'w', encoding='utf-8') as f:
                f.writelines(lines)

            pattern = re.compile(re.escape(stroke_by_rnd))
            with open('2txt_dnevnoy.txt', 'w', encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)

            #f.close()

            """# построчное чтение
            print('-------')
            with open("2txt_dnevnoy.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

        else:
            print('Nothing')


    zamena2()
    gc.collect()


def vecher():
    def count_lines(file):
        try:
            with open('3txt_vecher.txt', encoding='utf-8') as fl:
                return len(fl.readlines())
        except Exception:
            return 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    perem = count_lines(args.file)

    def zamena3():

        if perem == 0:
            print('Сделаю то')
            with open("3vecher_sps.txt", encoding='utf-8') as f:
                with open("3txt_vecher.txt", "w", encoding='utf-8') as f1:
                    for line in f:
                        f1.write(line)
            f.close()
            f1.close()

            """# построчное чтение
            print('-------')
            with open("3txt_vecher.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

            a = 1
            b = count_lines(args.file)
            rnd_numb = random.randint(a, b)
            stroke_by_rnd = ''
            stroke_by_rnd = linecache.getline("3txt_vecher.txt", rnd_numb)
            bot.send_message(chat_id, stroke_by_rnd)


            with open("3txt_vecher.txt", "r+", encoding='utf-8') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != stroke_by_rnd:
                        f.write(i)
                f.truncate()

            gc.collect()
        elif perem == 1:
            """# построчное чтение
            print('-------')
            with open("3txt_vecher.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

            #global last_stroke, str
            last_line = 'й'

            with open('3txt_vecher.txt', "r", encoding='utf-8') as f1:
                last_line = f1.readlines()[-1]
            print(last_line)

            bot.send_message(chat_id, last_line)

            readFile = open("3txt_vecher.txt", encoding='utf-8')
            lines = readFile.readlines()
            readFile.close()
            w = open("3txt_vecher.txt", 'w', encoding='utf-8')
            w.writelines([item for item in lines[:-1]])
            w.close()

        elif perem > 1:

            """#построчное чтение
            print('-------')
            with open("3txt_vecher.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            #end"""

            a = 1
            b = count_lines(args.file)
            # b = b - 1
            #print(b)
            rnd_numb = random.randint(a, b)
            stroke_by_rnd = 'й'
            stroke_by_rnd = linecache.getline("3txt_vecher.txt", rnd_numb)
            bot.send_message(chat_id, stroke_by_rnd)


            #print(stroke_by_rnd)

            with open('3txt_vecher.txt', encoding='utf-8') as f:
                lines = f.readlines()
                lines[rnd_numb - 1] = ''  # <- or whatever kind of newline is relevant for your system
            with open('3txt_vecher.txt', 'w', encoding='utf-8') as f:
                f.writelines(lines)

            pattern = re.compile(re.escape(stroke_by_rnd))
            with open('3txt_vecher.txt', 'w', encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)

            #f.close()

            """# построчное чтение
            print('-------')
            with open("3txt_vecher.txt", "r", encoding='utf-8') as file:
                for line in file:
                    print(line)
            print('--------')
            # end"""

        else:
            print('Nothing')


    zamena3()
    gc.collect()


print("End")




