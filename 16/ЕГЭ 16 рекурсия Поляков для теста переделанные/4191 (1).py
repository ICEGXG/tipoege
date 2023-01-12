# С какой цифры начинается дробная часть значения функции F(280)?
def f(n):
    if n == 0:
        return 8
    elif 0 < n <= 17:
        return f(n - 1)
    elif 17 < n < 100:
        return 2.5 * f(n - 3)
    elif n >= 100:
        return 3.3 * f(n - 4)
print(f(50))
print(int(f(50) // 0.1 % 10))



