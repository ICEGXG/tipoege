'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, если n < 4,
F(n) = n, если n > 3 и число n нечётное,
F(n) = F(n – 1) + F(n – 2) + F(n – 3), если n > 3 и число n чётное.
Чему равно значение выражения F(2258) – F(2249)?'''
from functools import *
@lru_cache(None)

def f(n):
    if n < 4: return 1
    if n > 3 and n % 2 != 0: return n
    if n > 3 and n % 2 == 0: return (f(n-1) + f(n-2) + f(n-3))

for n in range(1,3310):
    f(n)

print(f(2258) - f(2249))

# ответ 2544772
