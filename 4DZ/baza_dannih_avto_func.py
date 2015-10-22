# coding: utf-8
import pickle, os

avtomobili = []

komands = ['ввод','вывод','запись','имя','мощь','больше','меньше','промежуток','конец']

komand = ''

def vivod():
    print ('''
"ввод" - ввод данных в список
"вывод" - вывод данных из списка по алфавиту
"запись" - запись списка в базу данных
"имя" - поиск автомобиля по названию или части названия
"мощь" - поиск по мощи
"больше" - поиск по мощи, больше заданной
"меньше" - поиск по мощи, меньше заданной
"промежуток" - поиск авто по мощи в промежутке значений
"конец" - завершает работу программы''')

def vvod():
    komand = input('\nВведите одну из команд {}: '.format(komands)) 
    while komand not in komands:
        komand = input('Нет такой команды, введите еще раз :')  
    return komand


def vibor(i):
    print('\nВы выбрали {} данных'.format(komands[i]))


def vvod_avto():
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
        ext = input('''\nДля окончания ввода данных в базу, напишите "выход",
Для продолжения нажмите "Enter":''')


def vivod_avto():
    sort_avtomobili = sorted(avtomobili)
    for i in sort_avtomobili:
        print(i)


def zagr():
    f = open('c:/python/data_avto.txt', 'rb')
    avtos = pickle.load(f)
    return avtos


def zapis():
    f = open('c:/python/data_avto.txt', 'wb')
    sort_avtomobili = sorted(avtomobili)
    pickle.dump(sort_avtomobili,f)
    f.close


def name():
    imya = input('Введите часть имени или полное имя: ')
    for avto_mosh in avtos:
        if imya in avto_mosh:
            print(avto_mosh)


def konec():
    print('больше нет авто')


def mosh():
    mosh = int(input('Введите мощь авто: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if mosh == int(avmosh):
            print(avto_mosh)    


def bolshe():
    mosh = int(input('введите наименьшую мощь: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if int(avmosh) >= mosh:
            print(avto_mosh)


def menshe():
    mosh = int(input('введите наибольшую мощь: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if int(avmosh) <= mosh:
            print(avto_mosh)


def promeg():
    mosh1 = int(input('введите наименьшую мощь в промежутке: '))
    mosh2 = int(input('введите наибольшую мощь в промежутке: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if mosh1 <= int(avmosh) <= mosh2:
            print(avto_mosh)

vivod()

while komand != 'конец':

    komand = vvod()

    if komand == komands[0]:
        vibor(0)
        vvod_avto()

    if komand == komands[1]:
        vibor(1)
        vivod_avto()

    if komand == komands[2]:
        vibor(2)
        zapis()

    if komand == komands[3]:
        avtos = zagr()
        name()
        konec()

    if komand == komands[4]:
        avtos == zagr()
        mosh()
        konec()

    if komand == komands[5]:
        avtos == zagr()
        bolshe()
        konec()

    if komand == komands[6]:
        avtos == zagr()
        menshe()
        konec()

    if komand == komands[7]:
        avtos == zagr()
        promeg()
        konec()

    
        







