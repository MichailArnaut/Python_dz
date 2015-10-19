#a = [1,-20,38,0,44] 
#b = [88,-20,48,4,33,2]

k = 0
a = []
n = int(input('введите колличество элементов списка a: '))

while k < n:
    new_element = float(input('введите '+ str(k+1) + ' элемент '))
    a.append(new_element)
    k = k+1
    
k = 0    
b = []
n = int(input('введите колличество элементов списка b: '))

while k < n:
    new_element = float(input('введите '+ str(k+1) + ' элемент '))
    b.append(new_element)
    k = k+1
print('\n','a =',a,'\n','b =',b)

chisla = min(len(a), len(b)) 

i = 0
 
while i < chisla: 
 	print('числа', str(a[i]), 'и' , str(b[i])) 
 	print('наименьшее число' , str(min(a[i],b[i])))
 	print('модуль разности' , str(abs(a[i]-b[i])))
 	if (abs(a[i]-b[i])<15): 
 		print('модуль разности меньше 15,ПОЗДРАВЛЯЮ!') 
 	else: 
 		print('модуль разности больше 15,не поздравляю')
 	print('\n')	
 	i = i+1

