"""Класс прямоугольника."""

from .figure import Figure
from .color import FigureColor


class Rectangle(Figure):
    name = "Прямоугольник"

    def __init__(self, width, height, color):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными.")
        self.width = width
        self.height = height
        self.figure_color = FigureColor(color)

    def area(self):
        return self.width * self.height

    @classmethod
    def get_name(cls):
        return cls.name

    def __repr__(self):
        return "{}: ширина = {}, высота = {}, цвет = {}, площадь = {:.2f}".format(
            self.get_name(), self.width, self.height,
            self.figure_color.color, self.area()
        )

    def __str__(self):
        return self.__repr__()
