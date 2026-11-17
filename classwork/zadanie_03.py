# Задание 3
# Запуск: python zadanie_03.py

import time
import numpy as np
import math

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


# 3. sin(x) + x^2
def math_loop(x):
    result = []
    for v in x:
        result.append(math.sin(v) + v * v)
    return result


def math_np(x):
    return np.sin(x) + x ** 2


print('\n3. sin(x) + x^2')
r1, t1 = test(math_loop, a)
r2, t2 = test(math_np, a)
show(t1, t2)
print('Совпадает:', np.allclose(r1, r2))
print('Вывод: NumPy записывает формулу почти в одну строку.')
print('Код с циклом длиннее и обычно работает медленнее.')
del r1, r2
