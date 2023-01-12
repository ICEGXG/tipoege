# Сколько различных цифр встречается в целой части значения функции F(34)?
def f(n):
    if n == 0:
        return 5
    elif n > 0:
        if n % 2 == 0:
            return f(n - 1) + f(n - 2)
        else:
            return 1.7 * f(n - 1)
myset = set()  # задаем пустое множество
print(f(34))
x = int(f(34))  # без int тоже работает, но условие в цикле должно быть '> 0'
while x > 0:
    myset.add(x % 10)
    x //= 10
print(len(myset))



