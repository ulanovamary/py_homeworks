'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
import random, os

file = os.path.join(os.path.dirname(__file__),'les5_ht5_test.txt')
file = open('les5_ht5_test.txt', 'w', encoding='utf-8')

line = [random.randint(1, 100) for i in range(2, 10)]
print(line)
print(sum(line))

line_str = ' '.join(map(str, line))
print(line_str, type(line_str))
file.write(line_str)
file.close()

with open('les5_ht5_test.txt', 'r') as file:
    numbers = map(int, file.readline().split(' '))
    print(sum(numbers))


