# -*- coding: utf-8 -*-


from itertools import cycle
from time import sleep

class TrafficLight:
    colors_queue = ("красный", "желтый", "зеленый")
    time_queue = (7, 2, 5)
    message = ("Красный свет - проезда нет!", "Желтый - будь готов к пути", "А зеленый свет - кати")

    def __init__(self, color):
        self.__color = color

    def running(self):
        my_cycle = cycle(self.colors_queue)
        for traffic_color in my_cycle:
            if self.__color == traffic_color:
                print(self.message[self.colors_queue.index(self.__color)])
                sleep(self.time_queue[self.colors_queue.index(self.__color)])
                self.__color = next(my_cycle)

my_traffic = TrafficLight("желтый")
my_traffic.running()

