"""Точка входа в программу лабораторной работы № 2."""

from colorama import Fore, Style, init

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    init(autoreset=True)
    n = 10  

    rectangle = Rectangle(n, n, "синий")
    circle = Circle(n, "зелёный")
    square = Square(n, "красный")

    print(Fore.CYAN + "Лабораторная работа № 2. Геометрические фигуры")
    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()
