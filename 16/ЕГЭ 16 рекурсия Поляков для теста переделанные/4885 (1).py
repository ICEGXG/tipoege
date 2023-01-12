'''Определите сумму нечетных значений F(n) для всех n на отрезке [26,400]. В качестве ответа запишите количество цифр в десятичной записи этой суммы.
Примечание: необходимо использовать арифметику многоразрядных чисел.'''
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 11 * n + f(n - 1)
    else:
        return 11 * f(n - 3) + n
s = 0
for n in range(26, 401):
    if f(n) % 2 != 0:
        s += f(n)
print(len(str(s)))