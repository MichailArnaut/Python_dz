#coding: utf-8 
import os, sys


 
 
#Функция-генератор find 
 
 
def find (rash):
    for file in os.listdir('.'):
        if file.endswith(rash):
            for i, line in enumerate(open(file)): 
                yield file,i, line   
 
 
#Функция-генератор grep  
 
def grep (gen, sstring):
    for file, i, s in gen:
        if s.count(sstring):
            yield file, i, s 
             
 
 
 
for file, i, s  in grep (gen=find(rash=input('Введите расширение файла(например ".txt": ')), sstring =input('Введите данные для поиска: ')):
    print('Файл',file,'Строка', i, s) 
