# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
this_list = ['word', 23,(6,5,4), 45.98, None, [1,2,3], True]
'''print(type(this_list))
this_list.append(this_list)
this_list.extend(this_list)
this_list.insert(6,False) # position, element
this_list.remove(23) #elem
this_list.pop(5) #el index
print(this_list.index(45.98))
print(this_list.count((6,5,4)))
#print(this_list.sort()) #???
'''
print(this_list.reverse())
print(this_list.copy())
this_list.clear()
print(this_list)
