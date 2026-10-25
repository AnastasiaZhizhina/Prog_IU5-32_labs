"""Класс квадрата, производный от прямоугольника."""

from .rectangle import Rectangle


class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, side, color):
        if side <= 0:
            raise ValueError("Длина стороны должна быть положительной.")
        super().__init__(side, side, color)
        self.side = side

    @classmethod
    def get_name(cls):
        return cls.name

    def __repr__(self):
        return "{}: сторона = {}, цвет = {}, площадь = {:.2f}".format(
            self.get_name(), self.side,
            self.figure_color.color, self.area()
        )

    def __str__(self):
        return self.__repr__()
