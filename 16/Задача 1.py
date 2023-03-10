'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, если n = 1
F(n) = n·F(n – 1) + 1, если n > 1.
Чему равно значение выражения F(3297) // F(3294)? В ответе укажите только целую часть числа.'''
from functools import *
@lru_cache(None)

def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n-1) + 1

for n in range(1,3310):
    f(n)

print(f(3297) // f(3294))

# ответ 35806475040
