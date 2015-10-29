# coding: utf - 8

from db import zagr,zapis

komands = ['ввод','вывод','имя','мощь','больше','меньше','промежуток','конец']


def vivod():         # функция вывода возможных команд и их применение
    print ('''
"ввод" - ввод данных в список
"вывод" - вывод данных из списка по алфавиту
"имя" - поиск автомобиля по названию или части названия
"мощь" - поиск по мощи
"больше" - поиск по мощи, больше заданной
"меньше" - поиск по мощи, меньше заданной
"промежуток" - поиск авто по мощи в промежутке значений
"конец" - завершает работу программы''')


def vibor(i):
    print('\nВы выбрали {} данных'.format(komands[i]))


def vivod_avto():   # функция вывода отсортированного списка автомобилей
    vibor(1)
    avtomobili = zagr()
    sort_avtomobili = sorted(avtomobili)
    for i in sort_avtomobili:
        print(i)


def konec():
    print('больше нет авто')


def name():         # функция поиска авто по названию марки или части
    avtos = zagr() 
    imya = input('Введите часть имени или полное имя: ')
    for avto_mosh in avtos:
        if imya in avto_mosh:
            print(avto_mosh)
    konec()


def mosh():         # функция поиска авто по мощности
    avtos = zagr()
    mosh = int(input('Введите мощь авто: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if mosh == int(avmosh):
            print(avto_mosh)
    konec()


def bolshe():      # функция поиска авто по мощности больше заданной
    avtos = zagr()
    mosh = int(input('введите наименьшую мощь: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if int(avmosh) >= mosh:
            print(avto_mosh)
    konec()


def menshe():      # функция поиска авто по мощности меньше заданной
    avtos = zagr()
    mosh = int(input('введите наибольшую мощь: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if int(avmosh) <= mosh:
            print(avto_mosh)
    konec() 


def promeg():      # функция поиска авто по мощности в промежутке
    avtos = zagr()
    mosh1 = int(input('введите наименьшую мощь в промежутке: '))
    mosh2 = int(input('введите наибольшую мощь в промежутке: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if mosh1 <= int(avmosh) <= mosh2:
            print(avto_mosh)
    konec() 

