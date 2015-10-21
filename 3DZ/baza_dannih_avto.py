# coding: utf-8

import pickle 

avtomobili = []
komand = ''

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

komands = ['ввод','вывод','запись','имя','мощь','больше','меньше','промежуток','конец'] 


while komand != 'конец':
    
    komand = input('\nВведите одну из команд {}: '.format(komands))
    while komand not in komands:
        komand = input('Нет такой команды, введите еще раз :') 


#1 Ввод данных в список avtomobili состоящий из элементов 'марка мощность'

    if komand == komands[0]:    
        
        print('\nВы выбрали {} данных'.format(komands[0]))
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


#2 Вывод данных из отсортированного списка avtomobili (т.е. список sort_avtomobili)

    if komand == komands[1]:
        
        print('Вы выбрали {} данных'.format(komands[1]))
        sort_avtomobili = sorted(avtomobili)
        for i in sort_avtomobili:
                print(i)


#3 Запись(перезапись) данных в файл data_avto.txt из списка avtomobili 

    if komand == komands[2]:

        print('Вы выбрали {} данных'.format(komands[2]))
        f = open('c:/python/data_avto.txt', 'wb')    
        pickle.dump(avtomobili,f)
        f.close()


#4 Поиск по марке авто или части названия марки из данных запсанного файла data_avto.txt

    if komand == komands[3]:

        f = open('c:/python/data_avto.txt', 'rb')
        avtos = pickle.load(f)
        imya = input('Введите часть имени или полное имя: ')
        for avto_mosh in avtos:
            if imya in avto_mosh:
                print(avto_mosh)    
        print('больше нет авто')
        f.close()
        

#5 Поиск по конкретной мощности из данных файла data_avto.txt

    if komand == komands[4]:

        f = open('c:/python/data_avto.txt', 'rb')
        avtos = pickle.load(f)
        mosh = int(input('Введите мощь авто: '))
        for avto_mosh in avtos:
            avmosh = avto_mosh.split()[1]
            if mosh == int(avmosh):
                print(avto_mosh)
        print('больше нет авто')
        f.close()


#6 Поиск по мощностям, больше заданной, так же из данных data_avto.txt

    if komand == komands[5]:

        f = open('c:/python/data_avto.txt', 'rb')
        avtos = pickle.load(f)
        mosh = int(input('введите наименьшую мощь: '))
        for avto_mosh in avtos:
            avmosh = avto_mosh.split()[1]
            if int(avmosh) >= mosh:
                print(avto_mosh)
        print('больше нет авто')
        f.close()


#7 Поиск по мощностям, меньше заданной, из данных data_avto.txt

    if komand == komands[6]:
        
        f = open('c:/python/data_avto.txt', 'rb')
        avtos = pickle.load(f)
        mosh = int(input('введите наибольшую мощь: '))
        for avto_mosh in avtos:
            avmosh = avto_mosh.split()[1]
            if int(avmosh) <= mosh:
                print(avto_mosh)
        print('больше нет авто')
        f.close()


#8 Поиск по мощности в промежутке от мин(mosh1) до макс(mosh2) в данных из data_avto.txt

    if komand == komands[7]:

        f = open('c:/python/data_avto.txt', 'rb')
        avtos = pickle.load(f)
        mosh1 = int(input('введите наименьшую мощь в промежутке: '))
        mosh2 = int(input('введите наибольшую мощь в промежутке: '))
        for avto_mosh in avtos:
            avmosh = avto_mosh.split()[1]
            if mosh1 <= int(avmosh) <= mosh2:
                print(avto_mosh)
        print('больше нет авто')
        f.close()



        
        

        
        
