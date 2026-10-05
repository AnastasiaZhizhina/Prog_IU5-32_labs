import sys
import math


def read_coefficient(name, value_from_cmd=None):
    if value_from_cmd is not None:
        try:
            return float(value_from_cmd.replace(',', '.'))
        except ValueError:
            print(f"Некорректное значение {name} = '{value_from_cmd}'. Введите повторно.")

    while True:
        raw = input(f"Введите коэффициент {name}: ").strip().replace(',', '.')
        try:
            return float(raw)
        except ValueError:
            print(f"Ошибка: '{raw}' не является числом. Повторите ввод.")


def solve_biquadratic(a, b, c):
    if a == 0:
        if b == 0:
            return [] if c != 0 else ['any']
        t = -c / b
        if t < 0:
            return []
        if t == 0:
            return [0.0]
        root = math.sqrt(t)
        return [-root, root]

    d = b * b - 4 * a * c
    print(f"Дискриминант D = {d}")

    if d < 0:
        return []

    if d == 0:
        candidates = [-b / (2 * a)]
    else:
        sd = math.sqrt(d)
        candidates = [(-b - sd) / (2 * a), (-b + sd) / (2 * a)]

    roots = []
    for t in candidates:
        if t >= 0:
            r = math.sqrt(t)
            if r == 0:
                if 0.0 not in roots:
                    roots.append(0.0)
            else:
                roots.extend([-r, r])

    return sorted(set(round(x, 10) for x in roots))


def main():
    args = sys.argv[1:]
    a_raw = args[0] if len(args) > 0 else None
    b_raw = args[1] if len(args) > 1 else None
    c_raw = args[2] if len(args) > 2 else None

    print("Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0")

    a = read_coefficient('A', a_raw)
    b = read_coefficient('B', b_raw)
    c = read_coefficient('C', c_raw)

    print(f"\nУравнение: {a}*x^4 + {b}*x^2 + {c} = 0")

    roots = solve_biquadratic(a, b, c)

    if roots == ['any']:
        print("Бесконечно много решений.")
    elif not roots:
        print("Действительных корней нет.")
    else:
        print(f"Корней: {len(roots)}")
        for i, r in enumerate(roots, 1):
            print(f"  x{i} = {r}")


if __name__ == "__main__":
    main()