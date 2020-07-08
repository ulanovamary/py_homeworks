'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.

'''
class MyZEx(Exception):
    pass

class Some(Exception):
    def __init__(self, input_data, input_data2 ):
        self.input_data = input_data
        self.input_data2 = input_data2


    def zero_div(self):
        try:
            return int(self.input_data/self.input_data2)
        except (ZeroDivisionError, MyZEx):
            return 0


a = Some(10, 0)
print(a.zero_div())
q = Some(10, 2)
print(q.zero_div())





