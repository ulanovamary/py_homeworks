'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
'''
file = open('les5_ht4_test.txt', 'r+')
new_file = open('les5_ht4_test2.txt', 'w')

for el in file:
    if 'One' in el:
        el = el.replace('One', 'Один')
        new_file.write(el)
    elif 'Two'in el:
        el = el.replace('Two', 'Два')
        new_file.write(el)
    elif 'Three'in el:
        el = el.replace('Three', 'Три')
        new_file.write(el)
    elif 'Four' in el:
        el = el.replace('Four', 'Четыре')
        new_file.write(el)
file.close()
new_file.close()




