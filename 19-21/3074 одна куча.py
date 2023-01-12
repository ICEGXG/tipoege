def f(s,c,m):
    if s >= 1000:
        return c % 2 == m % 2
    if c == m:
        return 0
    if (c + 1)% 2 == m % 2:
        return f(s + 100, c + 1, m) or f(s * 2, c + 1, m)
    else:
        return f(s + 100, c + 1, m) and f(s * 2, c + 1, m)
k = 0
for s in range (1,1000):
    for m in range(1,5):
        if f(s,0,m) == 1:
            if m ==4 or m == 2:
                print(s,m)
                k += 1
            break
print(k)
# ответы 1 - 100, 2 - 150, 3 -  250 299
# 1 Петя   +100 *2     >= 1000 выигрыш
