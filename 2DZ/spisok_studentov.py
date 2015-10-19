# 1 Задание
# Создаем список. Заполняем его именами (+фамилиями).

k = 0
spisok = []
n = int(input('Введите колличество студентов:'))

for k in range(n):
    name_stud = input('\nВведите имя '+ str(k+1)+' студента:')
    famil_stud = input('Введите фамилию '+ str(k+1)+ ' студента:')
    spisok.append(name_stud +' '+ famil_stud)
    k = k+1
print('\n')
for name in spisok:
    print (name)


# 2 Задание
# Выводим имя студента через функцию input(). Выводим на экран студента по этому индексу.

nomer = int(input('\nВведите номер студента в списке(Индексация начинается с 1):'))
if nomer <= 0:
    nomer = int(input('Индексация по числам от 1, введите еще раз: '))
print (spisok[nomer-1])


# 3 Задание
# Выводим на экран имена нескольких студентов: через input() получаем начало и конец среза.

srez1 = int(input('\nВведите номер первого студента из среза по списку:'))
srez2 = int(input('Введите номер последнего студента из среза по списку:'))


print ('\nСписок студентов от ',srez1,'до',srez2,'студента:') # Выведет студентов по срезу, включающих эти индексы

for i in spisok[srez1-1:srez2]:
    print(i)


# 4 Задание
# Находим колличество студентов, в именах которых есть определенный символ или буква

simvol = input('\nВведите символ, который имеется в имени студента:')
vsego = 0
for student_name in spisok:
    if simvol in list(student_name):
        vsego= vsego + 1
    else:
        pass
print ('\nВсего студентов, в имени которых есть символ ',simvol,':',vsego)


# 5 Задание
# Находим группы студентов с одинаковыми именами и создаем списки этих групп.

names = []
spisok2 = []

for name_family in spisok:
    imya = name_family.split()[0]        # строка name_family в списке spisok разделяется по пробелу,тем самым получается новый список из имени и фамилии,
                                         #и берется 0-вой элемент из получившегося списка, т.е. имя

    if imya not in names:
        names.append(imya)               # в список с именами names добавляется имя
        spisok2.append([name_family])    # в список из списков добавляется новый список с именем и фамилией
    else:
        spisok2[names.index(imya)].append(name_family) # в элемент(список) списка spisok2, который находится по адресу имени из списка names,
                                                       #  добавляется имя и фамилия
        
print ('\nОтсортированный список по именам : \n')

for names in spisok2:
    print('\n')
    for name_family in names:
        print (name_family)




    
    
