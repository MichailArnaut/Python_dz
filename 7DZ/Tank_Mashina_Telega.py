# coding: utf-8 
import sys, os 
 
 
class tank:
    def __init__(self):
        self.model = input('Введите модель танка:')
        self.shassi = input('Есть ли шасси (есть или нет):')
        self.gus = input('Есть ли гусеницы (есть или нет):')
        self.skorost=int(input('Введите скорость танка:'))

    def status (self): 
        print ('Танк модели {} (наличие шасси: {}, наличие гусениц: {}) едет со скоростью {}'.format(self.model, self.shassi,self.gus,self.skorost)) 
 

 
class mashina:
    def __init__(self):
        self.model = input('Введите модель машины:')
        self.kolesa = int(input('Введите количество колес машины:'))
        self.skorost=int(input('Введите скорость машины:'))

    def status (self):
        print ('Автомобиль модели {} (колличество колес:{}) едет со скоростью {}'.format(self.model, self.kolesa,self.skorost)) 
 

 
class telega:
    def __init__(self):
        self.kolesa = int(input('Введите количество колес телеги:'))
        self.skorost=int(input('Введите скорость телеги:'))
        
    def status (self):
        print ('Телега(колличество колес:{}) едет со скоростью {}'.format(self.kolesa,self.skorost)) 
 

cars=[]

Tank=tank() 
Mash=mashina() 
Telega=telega() 
cars.append(Tank) 
cars.append(Mash) 
cars.append(Telega) 

 
for i in cars:
    print (i.status()) 

print('\nИзмененные введенных данных:\n')

#Изменение введенных данных:

Tank.skorost = 39  
Tank.shassi = 'нет'

Mash.skorost = 90
Mash.model = 'Audi'

Telega.skorost = 25
Telega.kolesa = 2

for i in cars:
    print (i.status()) 



 

