'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не
 включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''
import json

file = open('les5_ht7_test.txt', 'r')
profits = []
names =[]
for line in file:
    line_list = line.split()
    name = line_list[0]
    names.append(name)
    rev = line_list[2]
    costs = line_list[3]
    profit = int(rev) - int(costs)
    profits.append(profit)

    res = 0
    idx=0
    for el in profits:
        if int(el) >= 0:
            idx+=1
            res+=el
        else:
            pass

result_list = []
first_dict = {names[i]: profits[i] for i in range(len(profits))}
result_list.append(first_dict)
average_prof = {'average_profit': int(res/idx)}
result_list.append(average_prof)
file.close()

with open('les5_ht7_test.json', 'w') as write_f:
    json_result_list = json.dump(result_list, write_f)