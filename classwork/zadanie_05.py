# Задание 5
# Запуск: python zadanie_05.py

import time
import numpy as np

m = np.random.default_rng(42).normal(size=(100_000, 10))


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


# 5. Сумма по строкам
def rows_loop(x):
    result = []
    for i in range(len(x)):
        s = 0
        for j in range(10):
            s += x[i, j]
        result.append(s)
    return result


def rows_np(x):
    return x.sum(axis=1)


print('\n5. Сумма по строкам')
r1, t1 = test(rows_loop, m)
r2, t2 = test(rows_np, m)
show(t1, t2)
print('Совпадает:', np.allclose(r1, r2))
print('Строки кода (SLOC): цикл = 7, NumPy = 1')
print('Вывод: NumPy короче: одна строка вместо семи.')
print('axis=1 означает подсчёт суммы каждой строки.')
del r1, r2
