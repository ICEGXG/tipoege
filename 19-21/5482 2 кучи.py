# + 2  *2 1<= s <= 213
def f(a,b,c,m):
    if a + b >= 231:
        return c%2 == m % 2
    if c == m:
        return 0
    if (c + 1)% 2 == m % 2:
        return f(a + 2, b, c + 1, m) or f(a, b + 2, c + 1, m) or f(a * 2, b, c + 1, m) or f(a, b* 2, c + 1, m)
    else:
        return f(a + 2, b, c + 1, m) and f(a, b + 2, c + 1, m) and f(a * 2, b, c + 1, m) and f(a, b* 2, c + 1, m)
for b in range (1, 214):
    for m in range(1,5):
        if f(17, b, 0, m) == 1:
            print(b, m)
            break
# ответы 1 - 106, 2 - 53, 105, 3 - 96
