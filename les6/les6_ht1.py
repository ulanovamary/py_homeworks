import time

class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.running()

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = 'yellow'
        print(self.__color)
        time.sleep(2)
        self.__color = 'green'
        print(self.__color)
        time.sleep(4)

    #def col_change(self):


my_trafficlight = TrafficLight()
print(my_trafficlight.running())