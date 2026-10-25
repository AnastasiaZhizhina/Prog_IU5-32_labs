"""Класс, хранящий цвет фигуры."""


class FigureColor:
    """Цвет геометрической фигуры с доступом через свойство."""

    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        """Текущий цвет фигуры."""
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Цвет должен быть непустой строкой.")
        self._color = value.strip()
