# Задание 1
# Запуск: python zadanie_01.py

import time
import numpy as np

a = np.random.default_rng(42).normal(size=10_000_000)


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


# 1. Сумма массива
def sum_loop(x):
    s = 0
    for v in x:
        s += v
    return s


def sum_np(x):
    return x.sum()


print('\n1. Сумма массива')
print('n          Цикл (мс)   NumPy (мс)   Ускорение')
first = None
for n in [100_000, 1_000_000, 10_000_000]:
    r1, t1 = test(sum_loop, a[:n])
    r2, t2 = test(sum_np, a[:n])
    speed = t1 / t2
    print(f'{n:<10} {t1*1000:>10.2f}   {t2*1000:>10.2f}   {speed:>8.1f}x')
    print('Совпадает:', np.isclose(r1, r2))
    if speed > 10 and first is None:
        first = n
print('Вывод: NumPy быстрее, так как считает без медленного цикла Python.')
print('Первое n с ускорением больше 10x:', first if first else 'не найдено')
