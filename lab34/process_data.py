import json
import sys

from lab34.field import field
from lab34.unique import Unique
from lab34.gen_random import gen_random
from lab34.print_result import print_result
from lab34.cm_timer import cm_timer_1

# Путь к файлу: аргумент командной строки, иначе — рядом с этим скриптом
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    import os
    path = os.path.join(os.path.dirname(__file__), 'data_light.json')

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return [
        f"{profession}, зарплата {salary} руб."
        for profession, salary in zip(arg, salaries)
    ]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))