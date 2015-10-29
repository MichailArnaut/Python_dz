# coding: utf - 8

import sys
from db import zapis,zagr
from debug import vivod,vibor,vivod_avto,name,mosh,bolshe,menshe,promeg


komands = ['ввод','вывод','имя','мощь','больше','меньше','промежуток','конец']



def vvod():                  # функция выбора команды
    komand = input('\nВведите одну из команд {}: '.format(komands))  
    return komand


def proverka_vvoda(komand):  # проверка ввода команды
    while komand not in komands:
        komand = input('Нет такой команды, введите еще раз :')
    return komand


def zavershit():               # функция завершения работы программы
    komand = 'конец'
    return komand


def vvod_avto():             # функция ввода авто и мощности в список автомобилей
    vibor(0)
    avtomobili = zagr()
    ext = '' 
    while ext !='выход':
            
        marka = input('Введите марку автомобиля:')
        while marka.isalpha() is False:
                marka = input('Марка может состоять только из букв, введите еще раз:')
                
        moshnost =input('Введите мощность автомобиля:')
        while moshnost.isdigit() is False:
                moshnost = input('Мощность может состоять только из цифр, введите еще раз:')

        avtomobili.append(marka + ' ' + moshnost)
        print(avtomobili)
        zapis(avtomobili)
        ext = input('''\nДля окончания ввода данных в базу, напишите "выход",
Для продолжения нажмите "Enter":''')
    return avtomobili



FUNCS = {
    'ввод':vvod_avto,
    'вывод':vivod_avto,
    'имя':name,
    'мощь':mosh,
    'больше':bolshe,
    'меньше':menshe,
    'промежуток':promeg,
    'конец':zavershit
    }



# сама программа

vivod()
komand = ''
while komand != 'конец':

    komand = proverka_vvoda(vvod())
    FUNCS[komand]()

