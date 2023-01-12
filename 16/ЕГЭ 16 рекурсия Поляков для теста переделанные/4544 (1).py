'''Сколько различных значений может принимать функция F(n) для чисел n, меньших 5000?'''
def f(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 2 == 0:
            return f(n / 2) - 2
        else:
            return 4 + f(n - 1)

# так как нужны различные! значения, необходимо использовать множество

myset = set()  # создаем пустое множество
for n in range(0, 5000):  # обязательно от нуля
    myset.add(f(n))  # добавляем к множеству новый элемент
print(len(myset))  # выводим длину множества
print(myset)