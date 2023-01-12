''' укажите наибольшее значение n на отрезке [140, 205], для которого значение функции F(n) является простым числом?'''
def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return 7 * (n - 1) + f(n - 1)
def sc(x):  # вычисляем сумму цифр
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
def pr(x): # проверяем число на простоту
    flag = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            flag = False
            break  # обязательно делаем break, чтобы не затягивать вермя
    return flag
for n in range(140, 205):
    if pr(f(n)):
        print(f(n), n)
