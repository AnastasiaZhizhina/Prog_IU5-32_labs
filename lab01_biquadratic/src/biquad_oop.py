import sys
import math


class CoefficientReader:
    @staticmethod
    def read(name, cmd_value=None):
        if cmd_value is not None:
            try:
                return float(cmd_value.replace(',', '.'))
            except ValueError:
                print(f"Некорректное значение {name} = '{cmd_value}'. Введите вручную.")
        while True:
            raw = input(f"Введите коэффициент {name}: ").strip().replace(',', '.')
            try:
                return float(raw)
            except ValueError:
                print(f"Ошибка: '{raw}' не является числом. Повторите ввод.")


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = None
        self.roots = []
        self.infinite = False

    def solve(self):
        a, b, c = self.a, self.b, self.c

        if a == 0:
            if b == 0:
                self.infinite = (c == 0)
                return self.roots
            t = -c / b
            if t > 0:
                r = math.sqrt(t)
                self.roots = [-r, r]
            elif t == 0:
                self.roots = [0.0]
            return self.roots

        self.discriminant = b * b - 4 * a * c

        if self.discriminant < 0:
            return self.roots

        if self.discriminant == 0:
            candidates = [-b / (2 * a)]
        else:
            sd = math.sqrt(self.discriminant)
            candidates = [(-b - sd) / (2 * a), (-b + sd) / (2 * a)]

        result = []
        for t in candidates:
            if t >= 0:
                r = math.sqrt(t)
                if r == 0:
                    if 0.0 not in result:
                        result.append(0.0)
                else:
                    result.extend([-r, r])

        self.roots = sorted(set(round(x, 10) for x in result))
        return self.roots

    def __str__(self):
        return f"{self.a}*x^4 + {self.b}*x^2 + {self.c} = 0"


class ConsoleView:
    @staticmethod
    def show(eq):
        print(f"\nУравнение: {eq}")

        if eq.discriminant is not None:
            print(f"Дискриминант D = {eq.discriminant}")

        if eq.infinite:
            print("Бесконечно много решений.")
        elif not eq.roots:
            print("Действительных корней нет.")
        else:
            print(f"Корней: {len(eq.roots)}")
            for i, r in enumerate(eq.roots, 1):
                print(f"  x{i} = {r}")


def main():
    args = sys.argv[1:]
    a_raw = args[0] if len(args) > 0 else None
    b_raw = args[1] if len(args) > 1 else None
    c_raw = args[2] if len(args) > 2 else None

    print("Решение биквадратного уравнения")

    a = CoefficientReader.read('A', a_raw)
    b = CoefficientReader.read('B', b_raw)
    c = CoefficientReader.read('C', c_raw)

    eq = BiquadraticEquation(a, b, c)
    eq.solve()
    ConsoleView.show(eq)


if __name__ == "__main__":
    main()