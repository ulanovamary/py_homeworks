'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''
class Road:
    __mass_sqw_m = 25
    def __init__(self, length=5000, width=20):
        self._length = int(length)
        self._width = int(width)

    def mass_count(self, thickness=5):
        return self._length * self._width * self.__mass_sqw_m * thickness

#print(Road.mass_count())

second_road = Road()

print(second_road._width)
print(second_road.mass_count())