"""Класс круга."""

import math

from .figure import Figure
from .color import FigureColor


class Circle(Figure):
    name = "Круг"

    def __init__(self, radius, color):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным.")
        self.radius = radius
        self.figure_color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def get_name(cls):
        return cls.name

    def __repr__(self):
        return "{}: радиус = {}, цвет = {}, площадь = {:.2f}".format(
            self.get_name(), self.radius,
            self.figure_color.color, self.area()
        )

    def __str__(self):
        return self.__repr__()
