'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
file = open('les5_ht3_test.txt', 'r')
money_list = []
person_list = []

content = file.readlines()
for i in range(len(content)):
    person = content[i].split()[0]
    person_list.append(person)
    money = content[i].split()[1]
    money_list.append(int(money))

mid_sum = (sum(money_list))/len(money_list)
print('Средняя зп составляет: {}.'.format(mid_sum))
i=0
for idx, el in enumerate(money_list):
    if money_list[idx]<= 20000:
        print(person_list[idx])
file.close()