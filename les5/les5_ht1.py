'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
import os

file = os.path.join(os.path.dirname(__file__),'les5_ht1_test.txt')
file = open('les5_ht1_test.txt', 'w', encoding='utf-8')

str_list = []
line = None
while line != '':
    line = input('Введите строку: ')
    str_list.append(line)
for el in str_list:
    file.write(el+'\n')
print(str_list)

file.close()



