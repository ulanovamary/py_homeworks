#dict
winter = {'december':12, 'january':1, 'february':2}
spring = {'march':3, 'april':4, 'may':5}
summer = {'june':6, 'july':7, 'august':8}

month = int(input('Введите месяц года в цифровом значении от 1 до 12'))

if month in winter.values():
   print('Зима')
elif month in spring.values():
    print('Весна')
elif month in summer.values():
    print('Лето')
else:
    print('Осень')

#list
'''
month = int(input('Введите месяц года в цифровом значении от 1 до 12'))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]

if month in winter:
    print('Зима')
elif month in spring:
    print('Весна')
elif month in summer:
    print('Лето')
else:
    print('Осень')
'''
