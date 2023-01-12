'''Сколько существует значений n на отрезке [2, 200], для которых значение функции F(n) является простым числом?'''
def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return 7 * (n - 1) + f(n - 1)
def pr(x):  # проверяем число на простоту
    flag = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            flag = False
            break  # обязательно делаем break, чтобы не затягивать вермя
    return flag
k = 0
for n in range(2, 201):
    if pr(f(n)):
        print('*****', f(n))
        k += 1
print(k)