'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, если n = 1
F(n) = (2·n - 1)·F(n – 1), если n > 1.
Чему равно значение выражения F(3510) // F(3507)?'''
from functools import *
@lru_cache(None)

def f(n):
    if n == 1: return 1
    if n > 1: return (2*n-1)*f(n-1)

for n in range(1,3520):
    f(n)

print(f(3510) // f(3507))

# ответ 345505045845
