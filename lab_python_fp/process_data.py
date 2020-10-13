from lab_python_fp.gen_random import gen_random
from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.ptint_result import print_result
from lab_python_fp.cm_timer import cm_timer_1

import json
import sys

path = sys.argv[1]

with open(path) as file:
    data = json.load(file)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))
    # Сортируем уникальные значения по полям наимаенование работы без учета регистра


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startwith('программист'), arg))
    # Возвращаем отфильтрованные значения в которых значение работы начинается
    # с "программист", при этом делаем все в нижний регистр


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))
    # Модифицируем каждый выбранный в f2 элемент массива, добавив строку
    # 'с опытом Python' при помощи функции map


@print_result
def f4(arg):
    salary = list(gen_random(len(arg), 100000, 200000))
    # Генерируем зарплаты для каждого выбранного в массив программиста
    jobs = list(zip(arg, salary))
    return list(map(lambda x: x[0] + ', зарплата ' + str(x[1]) + ' руб.', jobs))


def main():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == "__main__":
    main()