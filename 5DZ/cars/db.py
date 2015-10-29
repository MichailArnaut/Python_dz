# coding: utf - 8

import sys, pickle


def zagr():    # функция открытия файла базы данных на чтение
    try:
        f = open('c:/python/data_avto.txt', 'rb')
        avtomobili = pickle.load(f)
    except FileNotFoundError:
        avtomobili = []
    return avtomobili


def zapis(avtomobili):    # функция записи списка автомобилей в файл базы данных 
    f = open('c:/python/data_avto.txt', 'wb')
    pickle.dump(avtomobili,f)
    f.close
    print('Запись произведена')
