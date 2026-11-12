# Задание 6
# Запуск: python zadanie_06.py

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


# 6. Вычитание среднего каждого столбца
def norm_loop(x):
    avg = [0] * 10
    for row in x:
        for j in range(10):
            avg[j] += row[j]
    for j in range(10):
        avg[j] /= len(x)
    result = []
    for row in x:
        result.append([row[j] - avg[j] for j in range(10)])
    return result


def norm_np(x):
    return x - x.mean(axis=0)


print('\n6. Нормировка столбцов')
r1, t1 = test(norm_loop, m)
r2, t2 = test(norm_np, m)
show(t1, t2)
print('Совпадает:', np.allclose(r1, r2))
print('Вывод: NumPy вычитает среднее сразу из каждого столбца.')
print('В обычном Python нужны циклы, поэтому код длиннее.')
del r1, r2
