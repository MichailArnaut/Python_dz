# coding: utf-8
import pickle, os


###   1 Задание    ### - преобразование части программ в функции
# п.с. при написании команды 'конец' завершится работа программы по 1 заданию, и начнется работа программы по 2 заданию и так далее...

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

def vvod():   # функция выбора команды
    komand = input('\nВведите одну из команд {}: '.format(komands))  
    return komand


def proverka_vvoda(komand):  # проверка ввода команды
    while komand not in komands:
        komand = input('Нет такой команды, введите еще раз :')
    return komand


def vibor(i):
    print('\nВы выбрали {} данных'.format(komands[i]))

def zapis():    # функция записи списка автомобилей в файл базы данных 
    f = open('c:/python/data_avto.txt', 'wb')
    pickle.dump(avtomobili,f)
    f.close
    print('Запись произведена')

def zapis2(x):    # функция перезаписи определенного объекта в файле
    f = open('c:/python/data_avto.txt', 'wb')
    pickle.dump(x,f)
    f.close
    print('Перезапись произведена')    


def zagr():    # функция открытия файла базы данных на чтение
    try:
        f = open('c:/python/data_avto.txt', 'rb')
        avtomobili = pickle.load(f)
    except IOError:
        avtomobili = []
    return avtomobili

    
def vvod_avto():   # функция ввода авто и мощности в список автомобилей
    vibor(0)
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
    return avtomobili


def vivod_avto():   # функция вывода отсортированного списка автомобилей
    vibor(1) 
    sort_avtomobili = sorted(avtomobili)
    for i in sort_avtomobili:
        print(i)


def konec():
    print('больше нет авто')


def name():   # функция поиска авто по названию марки или части
    avtos = zagr() 
    imya = input('Введите часть имени или полное имя: ')
    for avto_mosh in avtos:
        if imya in avto_mosh:
            print(avto_mosh)
    konec()




def mosh(): # функция поиска авто по мощности
    avtos = zagr()
    mosh = int(input('Введите мощь авто: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if mosh == int(avmosh):
            print(avto_mosh)
    konec()


def bolshe():   # функция поиска авто по мощности больше заданной
    avtos = zagr()
    mosh = int(input('введите наименьшую мощь: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if int(avmosh) >= mosh:
            print(avto_mosh)
    konec()


def menshe():   # функция поиска авто по мощности меньше заданной
    avtos = zagr()
    mosh = int(input('введите наибольшую мощь: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if int(avmosh) <= mosh:
            print(avto_mosh)
    konec() 


def promeg():  # функция поиска авто по мощности в промежутке
    avtos = zagr()
    mosh1 = int(input('введите наименьшую мощь в промежутке: '))
    mosh2 = int(input('введите наибольшую мощь в промежутке: '))
    for avto_mosh in avtos:
        avmosh = avto_mosh.split()[1]
        if mosh1 <= int(avmosh) <= mosh2:
            print(avto_mosh)
    konec() 

vivod()

while komand != 'конец':

    komand = proverka_vvoda(vvod())

    if komand == komands[0]:
        vvod_avto()

    if komand == komands[1]:
        vivod_avto()

    if komand == komands[2]:
        zapis()

    if komand == komands[3]:
        name()
        
    if komand == komands[4]:
        mosh()

    if komand == komands[5]:
        bolshe()

    if komand == komands[6]:
        menshe()

    if komand == komands[7]:
        promeg()


    
###   2 Задание    ### - добавление команд и их функций в словарь

def zavershit():
    komand = 'конец'
    return komand

# komands = ['ввод','вывод','запись','имя','мощь','больше','меньше','промежуток','конец']

FUNCS = {
    'ввод':vvod_avto,
    'вывод':vivod_avto,
    'запись':zapis,
    'имя':name,
    'мощь':mosh,
    'больше':bolshe,
    'меньше':menshe,
    'промежуток':promeg,
    'конец':zavershit
    }

vivod()
komand = ''
while komand != 'конец':

    komand = proverka_vvoda(vvod())
    FUNCS[komand]()
    

###   3 Задание    ### - добавление операций редактирование по мощности и удаление авто из файла с базой данных

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
"удаление" - изменяет мощность авто в базе данных
"редактирование" - удаляет авто из базы данных
"конец" - завершает работу программы''')

def ydal():
    avtomobili = zagr()
    print (avtomobili)
    vibor(8)
    imya = input('Введите полностью марку авто: ')
    mosh = input('Введите мощность авто: ')
    for avto_mosh in avtomobili:
        avname,avmosh = avto_mosh.split()
        if imya == avname and mosh == avmosh:
            avtomobili.remove(avto_mosh)
    zapis2(avtomobili)

def redakt():
    avtomobili = zagr()
    print (avtomobili)
    vibor(9)
    imya = input('Введите полностью марку авто: ')
    mosh = input('Введите мощность авто: ')
    mosh2 =input('Введите новую мощность авто: ')
    for avto_mosh in avtomobili:
        avname,avmosh = avto_mosh.split()
        if imya == avname and mosh == avmosh:
            avtomobili.remove(avto_mosh)
            avtomobili.append(avname + ' ' + mosh2)
    zapis2(avtomobili)
    
komands = ['ввод','вывод','запись','имя','мощь','больше','меньше','промежуток','удаление','редактирование','конец']

FUNCS = {
    'ввод':vvod_avto,
    'вывод':vivod_avto,
    'запись':zapis,
    'имя':name,
    'мощь':mosh,
    'больше':bolshe,
    'меньше':menshe,
    'промежуток':promeg,
    'удаление':ydal,
    'редактирование':redakt,
    'конец':zavershit
    }

vivod()
komand = ''
while komand != 'конец':

    komand = proverka_vvoda(vvod())
    FUNCS[komand]()









