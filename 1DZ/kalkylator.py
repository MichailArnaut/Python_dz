print('''                        Калькулятор
    Ноль в качестве знака операции завершит работу программы''')
while True:
    s = input('''
Введите одну из операций:
+
-
*
/
**(возведение в степень)

: ''')
    if s== '0': break 
    if s in ('+','-','*','/','**'):
        x = float(input('x = '))
        y = float(input('y = '))
        if s == '+':
            print('= ',x+y,'\n')
        if s == '-':
            print('= ',x-y,'\n')
        if s == '*':
            print('= ',x*y,'\n')
        if s == '/':
            if y != 0:
                print('= ',x/y,'\n')
            else: print('Деление не ноль не возможно!')
        if s == '**':
            print('= ',x**y,'\n')
    else: print('Неверная операция!')
