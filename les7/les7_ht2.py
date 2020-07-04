'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

class Clothes:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __add__(self, other):
        return self.size + other.size


class Coat(Clothes):
    @property
    def t_consumption_coat(self):
        self.size = (self.size/6.5) + 0.5
        return self.size


class Suit(Clothes):
    @property
    def t_consumption_suit(self):
        self.size = (2 * self.size) + 0.3
        return self.size

coat1 = Coat('пальтишко', 34)
print(coat1.t_consumption_coat)

suit2 = Suit('костюмчик', 36)
print(suit2.t_consumption_suit)

print(suit2.__add__(coat1))
