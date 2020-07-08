'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами
выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''
class SomeEx(Exception):
    pass

class MyEx(Exception):
    pass
    #def __init__(self, my_list:list):
        #self.my_list = my_list

class SomeValid(Exception):
    def validation(self=None):
        my_list = []
        while True:
            i = input('enter a digit or press q to stop')
            if i.isdigit() is True:
                my_list.append(i)
            elif i == 'q':
                print(my_list)
                break
            else:
                print(my_list)
                raise SomeEx(f'Not digit was entered {i}')

a = SomeValid
a.validation()




''' def to_my_list(self):
        self.my_list = []
        for i in self.my_list:
            try:
                while i != 'q':
                    i = input('enter a digit or press q to stop2')
                    if int(i).isdigit():
                        self.my_list.append(i)
                    else:
                        print('enter a digit')
            except ValueError as e:
                print('e')
        print(self.my_list)

a = MyEx()
print(a.to_my_list())
'''


