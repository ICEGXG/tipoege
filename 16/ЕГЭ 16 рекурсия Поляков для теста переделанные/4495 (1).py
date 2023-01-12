
'''Для какого значения n значение F(n) будет равно 49507?'''
def f(n):
    if n <= 2 or n == 9:
        return 0
    elif n == 3:
        return 1
    else:
        return f(n - 3) + f(n - 1)
n = 0
while True:
    #print(f(n))
    if f(n) == 49507:
        print(n)
        break
    n += 1



