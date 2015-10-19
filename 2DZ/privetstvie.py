name = input('Введите аше имя : ')

from datetime import datetime
current = datetime.now()
hour = current.hour
minute = current.minute

privetstvie = 'Здравствуйте, {}. Вы вошли в {} часов {} минут'
print (privetstvie.format(name,hour,minute))
