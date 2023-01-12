'''Сколько существует чисел n, меньших 1000, для которых значение F(n) будет равно -2?'''
def f(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 2 == 0:
            return f(n / 2) - 2
        else:
            return 2 + f(n - 1)

k = 0
for n in range(0, 1000):  # обязательно от нуля
    if f(n) == -2:
        k += 1
print(k)