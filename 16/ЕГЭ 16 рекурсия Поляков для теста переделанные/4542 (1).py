'''Сколько существует чисел n, меньших 1500, для которых значение F(n) будет равно -8?'''
def f(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 2 == 0:
            return f(n / 2) - 2
        else:
            return 4 + f(n - 1)
k = 0
for n in range(100, 1401):  # обязательно от нуля
    print(f(n))
    if f(n) == -8:
        k += 1
print('****', k)