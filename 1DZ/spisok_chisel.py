import math 

lst = [1,12,3,3,4,3,12,16,23,45]
f = open('c:\papka\chisla.txt','w')
for i in lst:
    f.write(str(i))
    f.write('\n')
f.close()

f = open("c:\papka\chisla.txt",'r')

list = f.read().split()
 
for i in list: 
    print(i) 
 
summa = float(list[0]) + float(list[1])
print('Сумма первого и второго числа = ',summa) 

proizvedenie = math.sqrt(float(list[2])*float(list[3])) 
print('Корень из произведения 3-го и 4-го числа = ',proizvedenie) 

if summa >= proizvedenie:
    print('Максимум = ',summa)
else:
    print ('Максимум = ',proizvedenie)
 
cosinus = math.cos(float(list[4])) 
 
print('Косинус 5-го числа = ', cosinus) 

f.close() 
