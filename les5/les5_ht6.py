'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
file = open('les5_ht6_test.txt', 'r',)
title = []
hours = []

for line in file:
    line_lst = line.split()
    subject = line_lst[0]
    subject = subject[:len(subject)-1]
    elem = line_lst[1:]
    result = 0
    for elem in line_lst[1:]:
        if '(' in elem:
            elem = elem[0:elem.index('(')]
            result += int(elem)
    hours.append(result)
    title.append(subject)

print(title)
print(hours)

study_dict = {title[i]: hours[i] for i in range(len(title))}
print(study_dict)