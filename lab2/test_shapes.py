"""Модульные тесты классов геометрических фигур."""

import math
import unittest

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.color import FigureColor


class TestShapes(unittest.TestCase):
    def test_rectangle_area_and_name(self):
        figure = Rectangle(3, 4, "синий")
        self.assertEqual(figure.area(), 12)
        self.assertEqual(figure.get_name(), "Прямоугольник")
        self.assertIn("площадь = 12.00", repr(figure))

    def test_circle_area(self):
        figure = Circle(2, "зелёный")
        self.assertAlmostEqual(figure.area(), math.pi * 4)
        self.assertEqual(figure.get_name(), "Круг")

    def test_square_area_and_inheritance(self):
        figure = Square(5, "красный")
        self.assertIsInstance(figure, Rectangle)
        self.assertEqual(figure.area(), 25)
        self.assertEqual(figure.get_name(), "Квадрат")
        self.assertIn("сторона = 5", repr(figure))

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, "синий")
        with self.assertRaises(ValueError):
            Circle(-1, "зелёный")
        with self.assertRaises(ValueError):
            Square(0, "красный")

    def test_color_property(self):
        color = FigureColor("синий")
        self.assertEqual(color.color, "синий")
        color.color = "жёлтый"
        self.assertEqual(color.color, "жёлтый")
        with self.assertRaises(ValueError):
            color.color = ""


if __name__ == "__main__":
    unittest.main()
