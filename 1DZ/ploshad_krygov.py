import math
pi = math.pi
t1 = float(input('Введите диагональ 1 круга: '))
t2 = float(input('Введите диагональ 2 круга: '))
t3 = float(input('Введите диагональ 3 круга: '))
s1 = pi*(t1/2)**2
s2 = pi*(t2/2)**2
s3 = pi*(t3/2)**2
print(' S1= ',s1,'\n','S2= ',s2,'\n','S3= ',s3,'\n' )
print('S3-(S1+S2)= ',s3 - (s1 + s2))
