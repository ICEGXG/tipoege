# С какой цифры начинается дробная часть значения функции F(100)?
def f(n):
    if n == 0:
        return 3
    elif 0 < n <= 15:
        return f(n - 1)
    elif 15 < n < 100:
        return 2.5 * f(n - 3)
    elif n >= 100:
        return 3.3 * f(n - 2)
print(f(100))
print(int(f(100) // 0.1 % 10))



