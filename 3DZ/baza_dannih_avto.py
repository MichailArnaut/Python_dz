# coding: utf-8

import pickle 

 
komands = ['ввод','вывод','запись','','',''] 



 
komand = input('Введите одну из команд {}: '.format(komands))
while komand not in komands:
    komand = input('Нет такой команды, введите еще раз :')


avtomobili = []

while komand in komands:
        
    if komand == komands[0]:
        
        print('Вы выбрали {} данных'.format(komands[0]))
        ext = '' 
        while ext !='выход':
            
            marka = input('Введите марку автомобиля:')
            while marka.isalpha() is False:
                    marka = input('Марка может состоять только из букв, введите еще раз:')
                    
            moshnost =input('Введите мощьность автомобиля:')
            while moshnost.isdigit() is False:
                    moshnost = input('Мощьность может состоять только из цифр, введите еще раз:')

            avtomobili.append(marka + ' ' + moshnost)
            print(avtomobili)
            ext = input('''Для окончания ввода данных в базу, напишите "выход",
Для продолжения нажмите "Enter":''')
            
        komand = input('Введите одну из команд {}: '.format(komands))
        while komand not in komands:
            komand = input('Нет такой команды, введите еще раз :')

    if komand == komands[1]:
        
        print('Вы выбрали {} данных'.format(komands[1]))
        sort_avtomobili = sorted(avtomobili)
        for i in sort_avtomobili:
                print(i)
        
        komand = input('Введите одну из команд {}: '.format(komands))
        while komand not in komands:
            komand = input('Нет такой команды, введите еще раз :')


    

       
 

