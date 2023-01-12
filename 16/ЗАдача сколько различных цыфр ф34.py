def f(n):
    if n == 0:
        return 5
    if n % 2 == 0 and n > 0:
        return f(n-1) + f(n-2)
    if n % 2 != 0 and n > 0:
        return 17 * f(n-1)
s = str(f(34))
print(s)
m = set(s)
print(len(m))
