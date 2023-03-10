'''(№ 5731) (А. Кабанов) Алгоритм вычисления значения функции F(n),
где n – натуральное число, задан следующими соотношениями:
F(n) = n, если n ≥ 10 000,
F(n) = n/4 + F(n/4 + 2), если n < 10 000 и n делится на 4,
F(n) = 1 + F(n + 2) , если n < 10 000 и n не делится на 4.
Чему равно значение выражения F(174) – F(3)?'''
from functools import * # для кэширования
@lru_cache(None)        # для кэширования
def  f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 4  == 0:
        return n//4 + f(n//4 + 2)
    if n < 10000 and n % 4  != 0:
        return 1 + f(n + 2)

for n in range(10000,1,-1):    # этот цикл сорхраняет в кэш значения функции     
    if  n % 4 != 0 and n % 2 != 0 : 
        f(n)
for n in range(10000,1,-1):    # этот цикл сорхраняет в кэш значения функции
    f(n)
print(f(174) - f(3))
print(f(174), f(3))
for i in range(1,20):
    print(f(i))
# 
