'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
   который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
'''
import random

class Car():
    def __init__(self, speed, color, name, is_police:bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        i = random.randint(1, 25)
        if int(i) % 2 == 0:
            print('Машина повернула направо')
        else:
            print('Машина повернула налево')

    def show_speed(self):
        print(f'Скорость {random.randint(20,150)} км/ч')


class TownCar(Car):

    def show_speed(self):
        i = random.randint(20,150)
        if i > 60:
            print(f'Привышение скорости town car! {i}!!')
        else:
            print(f'Скорость town car {i} км/ч')

class SportCar(Car):

 class WorkCar(Car):

     def show_speed(self):
         i = random.randint(20, 150)
         if i > 40:
             print(f'Привышение скорости work car! {i}')
         else:
             print(f'Скорость work car {i} км/ч')

 class PoliceCar():
     pass

 wcar = WorkCar(60, 'red', 'ford', False)
 wcar.stop()
 print(wcar.is_police)
 wcar.turn()
 print(wcar.color)


