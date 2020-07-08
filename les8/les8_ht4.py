'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
 уникальные для каждого типа оргтехники.
'''
class Stock:
    def __init__(self, list_eq:list):
        self.list_eq = list_eq

    def to_keep(self, *items):
       self.list_eq = {'название':{}}


class OfficeEquipment:
    def __init__(self, title, trade_mark, price, quantity):
        self.title = title
        self.trade_mark = trade_mark
        self.price = price
        self.quantity = quantity

class Printer(OfficeEquipment):
        def __init__(self, touchpad:bool):
            super().__init__(self.title, self.trade_mark, self.price, self.quantity)
            self.touchpad = touchpad


class Scaner(OfficeEquipment):
    def __init__(self, color:str):
        super().__init__(self.title, self.trade_mark, self.price, self.quantity)
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self, screen:bool):
        super().__init__(self.title, self.trade_mark, self.price, self.quantity)
        self.screen = screen


