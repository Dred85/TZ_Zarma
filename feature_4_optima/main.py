import timeit
import numpy as np


def compute_squares_append():
    """Вычисление через append"""
    numbers = [i for i in range(1, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)


def compute_squares_listcomp():
    """Вычисление через списочное выражение"""
    numbers = range(1, 1000001)
    squares = [number ** 2 for number in numbers]


def compute_squares_numpy():
    """Вычисление через библиотеку numpy"""
    numbers = np.arange(1, 1000001)
    squares = numbers ** 2


# Замер времени выполнения
append_time = timeit.timeit(compute_squares_append, number=10)
listcomp_time = timeit.timeit(compute_squares_listcomp, number=10)
np_time = timeit.timeit(compute_squares_numpy, number=10)

print(f"Время выполнения исходного скрипта: {append_time} секунд")
print(f"Время выполнения list comprehension: {listcomp_time} секунд")
print(f"Время выполнения compute_squares_numpy: {np_time} секунд")
