# Задание 2
# Запуск: python zadanie_02.py

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


# 2. Среднее и стандартное отклонение
def mean_loop(x):
    s = 0
    sq = 0
    for v in x:
        s += v
        sq += v * v
    avg = s / len(x)
    std = (sq / len(x) - avg * avg) ** 0.5
    return avg, std


def mean_np(x):
    return x.mean(), x.std()


print('\n2. Среднее и стандартное отклонение')
r1, t1 = test(mean_loop, a)
r2, t2 = test(mean_np, a)
show(t1, t2)
print('Совпадает до 1e-12:', abs(r1[0] - r2[0]) < 1e-12 and abs(r1[1] - r2[1]) < 1e-12)
print('Вывод: NumPy проще: достаточно mean() и std().')
print('В цикле приходится самостоятельно считать сумму и квадраты.')
