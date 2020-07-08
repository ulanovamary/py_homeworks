'''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
 Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
'''
import random

class Stock:
    list_eq = {}

    @staticmethod
    def dep():
        depts = ['Dep1', 'Dep2', 'Dep3']
        return random.choice(depts)

    @classmethod
    def to_add(cls, other):
        cls.other = []
        if other.title in cls.list_eq:
            cls.list_eq[other.title][1] += other.quantity
        else:
            cls.list_eq[other.title] = [other.price, other.quantity]
            print(f'Техника {other.title} поступила на склад\n'
                f'Количество этой техники на складе: {cls.list_eq[other.title][1]}')

    @classmethod
    def to_move(cls):
        for item in cls.list_eq.items():
            title = item[0]
            if title == 'printer':
                if cls.list_eq[title][1] == 0:
                    print(f'Нет техники {title} ')
                else:
                    cls.list_eq[title][1] -= 1
                    print(f'Техника {title} отправлена в  {Stock.dep()}')
            if title == 'scaner':
                if cls.list_eq[title][1] == 0:
                    print(f'Нет техники {title} ')
                else:
                    cls.list_eq[title][1] -= 1
                    print(f'Техника {title} отправлена в {Stock.dep()}')
            if title == 'xerox':
                if cls.list_eq[title][1] == 0:
                    print(f'Нет техники {title}')
                else:
                    cls.list_eq[title][1] -= 1
                    print(f'Техника {title} отправлена в {Stock.dep()}')

class OfficeEquipment:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

class Printer(OfficeEquipment):
        def __init__(self, title, price, quantity, touchpad:bool):
            self.title = title
            self.price = price
            self.quantity = quantity
            self.touchpad = touchpad


class Scaner(OfficeEquipment):
    def __init__(self, title, price, quantity, color:str):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self,title, price, quantity, screen:bool):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.screen = screen

print1 = Printer('printer', 2000, 3, True)
scan1 = Scaner('scaner', 1000, 1, 'color')
xer1 = Xerox('xerox', 22222, 11, True)
#print(print1.__dict__)

my_l = [print1, scan1, xer1]
for el in my_l:
    Stock.to_add(el)
    print()

print(Stock.list_eq)
for item in Stock.list_eq.items():
    Stock.to_move()


