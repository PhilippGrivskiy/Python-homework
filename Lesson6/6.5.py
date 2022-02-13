#-*- coding: utf-8 -*-

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):

    def draw(self):
        print(f'We are drawing by {self.title}')

class Pencil(Stationary):

    def draw(self):
        print(f"We are drawing by {self.title}")

class Handle(Stationary):

    def draw(self):
        print(f'We are drawing by {self.title} ')

pen = Pen("pen")





pencil = Pencil("pencil")
handle = Handle("handle")
pen.draw()
pencil.draw()
handle.draw()