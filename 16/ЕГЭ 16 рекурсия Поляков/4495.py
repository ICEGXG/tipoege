
'''Для какого значения n значение F(n) будет равно 25?'''
def f(n):
    if n <= 2 or n == 8:
        return 0
    elif n == 3:
        return 1
    else:
        return f(n - 2) + f(n - 1)
n = 0
while True:  # обязательно от нуля
    if f(n) == 25:
        print(n)
        break
    n += 1



