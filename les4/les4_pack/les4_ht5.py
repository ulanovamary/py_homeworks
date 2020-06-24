'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce

my_list = [el for el in range(99, 1001) if el%2 ==0]

def my_func(el,next_el):
    return el+next_el

print(my_list)

print(reduce(my_func, my_list))


