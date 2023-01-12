'''Сколько существует значений n на отрезке [1, 20], для которых сумма цифр значения функции F(n) является простым числом?'''
def f(n):
    if n <= 1:
        return 2
    elif n % 3 == 0:
        return 2 * f(n - 1) + f(n - 2)
    else:
        return 3 * f(n - 2) + f(n - 1) + 1
def sc(x):  # вычисляем сумму цифр
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
def pr(x):  # проверка числа на простоту
    flag = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            flag = False
            break  # обязательно делаем break, чтобы не затягивать вермя
    return flag
k = 0
for n in range(1, 20):
    print(f(n))
    if pr(f(n)):
        k += 1
        print('***', f(n))
print(k)