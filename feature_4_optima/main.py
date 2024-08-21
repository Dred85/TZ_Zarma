import timeit
import numpy as np

numbers = np.arange(1, 1000001)
squares = numbers ** 2


def compute_squares_append():
    numbers = [i for i in range(1, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)


def compute_squares_listcomp():
    numbers = range(1, 1000001)
    squares = [number ** 2 for number in numbers]


def compute_squares_np():
    numbers = np.arange(1, 1000001)
    squares = numbers ** 2


# Замер времени выполнения
append_time = timeit.timeit(compute_squares_append, number=10)
listcomp_time = timeit.timeit(compute_squares_listcomp, number=10)
generator_time = timeit.timeit(compute_squares_np, number=10)

print(f"Время выполнения map: {append_time} секунд")
print(f"Время выполнения list comprehension: {listcomp_time} секунд")
print(f"Время выполнения compute_squares_listcomp: {generator_time} секунд")
