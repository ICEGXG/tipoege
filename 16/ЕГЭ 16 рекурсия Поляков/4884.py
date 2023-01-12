'''Сколько существует значений n на отрезке [1, 35], для которых сумма цифр значения функции F(n) является простым числом?'''
def f(n):
    if n <= 1:
        return 1
    elif n % 3 == 0:
        return 2 * f(n - 1) + f(n - 2)
    else:
        return 3 * f(n - 2) + f(n - 1)
def sc(x):  # вычисляем сумму цифр
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
def pr(x):  # проверка числа на простоту
    flag = True
    for i in range(2, int(x**0.5) + 1):  # от 2 до корня из x + 1
        if x % i == 0:
            flag = False
            break  # обязательно делаем break, чтобы не затягивать вермя
    return flag
k = 0
for n in range(1, 36):
    print(f(n))
    x = f(n)
    if pr(x) == True:
        k += 1
        print('****', f(n))
print(k)