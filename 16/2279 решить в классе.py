def f(n):
    if n <= 3:
        return n # возврат значения ()
    if n > 3 and n % 2 == 0:
        return n + 3 + f(n - 1)
    if n > 3 and n % 2 != 0:
        return n * n + f(n - 2)
k = 0
for n in range(1, 1001):
    a = f(n)# на всякий случай записываем функцию в переменную
    if a % 7 == 0:
        k += 1
print(k)
