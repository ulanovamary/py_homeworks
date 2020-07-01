'''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
 (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов
  методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод
  для каждого экземпляра.
'''
class Stationary():
    def __init__(self, title):
        self.title = title


    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationary):

    def draw(self):
        print('Запуск отрисовки маркером')

pen1 = Pen
pencil1 = Pencil
handle1 = Handle
pen1.draw('ручечка')
pencil1.draw('карандашик')
handle1.draw('маркерочек')