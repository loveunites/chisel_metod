# Задание 7
# Запуск: python zadanie_07.py

import time
import numpy as np

a = np.random.default_rng(42).normal(size=1_000_000)


def test(func, data, change=False):
    best = float('inf')
    answer = None
    for _ in range(3):
        x = data.copy() if change else data
        start = time.perf_counter()
        result = func(x)
        seconds = time.perf_counter() - start
        if seconds < best:
            best = seconds
            answer = result
    return answer, best


def show(t1, t2):
    print(f'Цикл: {t1 * 1000:.2f} мс')
    print(f'NumPy: {t2 * 1000:.2f} мс')
    print(f'Ускорение: {t1 / t2:.1f}x')


# 7. Поиск максимума и индекса
def max_loop(x):
    biggest = x[0]
    index = 0
    for i in range(len(x)):
        if x[i] > biggest:
            biggest = x[i]
            index = i
    return biggest, index


def max_np(x):
    return x.max(), x.argmax()


print('\n7. Максимум и индекс')
r1, t1 = test(max_loop, a)
r2, t2 = test(max_np, a)
show(t1, t2)
print('Совпадает:', r1 == r2)
print('Вывод: max() и argmax() сразу находят число и его индекс.')
print('Так проще, чем хранить их вручную в цикле.')
