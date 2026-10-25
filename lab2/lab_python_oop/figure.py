"""Абстрактный базовый класс геометрической фигуры."""

from abc import ABC, abstractmethod


class Figure(ABC):
    """Общий интерфейс геометрических фигур."""

    @abstractmethod
    def area(self):
        """Вернуть площадь фигуры."""
        raise NotImplementedError
