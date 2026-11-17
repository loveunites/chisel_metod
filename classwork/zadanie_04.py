# Задание 4
# Запуск: python zadanie_04.py

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


# 4. Ограничение значений от 0 до 1
def clip_loop(x):
    result = []
    for v in x:
        if v < 0:
            v = 0
        elif v > 1:
            v = 1
        result.append(v)
    return result


def clip_np(x):
    return np.clip(x, 0, 1)


print('\n4. Замена значений')
r1, t1 = test(clip_loop, a)
r2, t2 = test(clip_np, a)
show(t1, t2)
print('Совпадает:', np.array_equal(r1, r2))
print('Изменено элементов:', np.sum((a < 0) | (a > 1)))
print('Вывод: np.clip() заменяет несколько условий одной командой.')
print('Это короче и понятнее обычного цикла.')
del r1, r2
