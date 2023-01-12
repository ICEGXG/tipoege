# +3  *2  выигрыш >= 33 кам. в начале 1<=s<=32
def f(s,c,m): # s - начальное количество камней,
    #с - счетчик ходов, номер, которым мы ограничиваем игру
    if s >= 33:
        return c%2 == m%2
    if c == m:
        return 0
    if (c + 1)%2 == m%2:
        return f(s + 3, c + 1, m) or f(s * 2, c + 1, m)
    else:
        return f(s + 3, c + 1, m) and f(s * 2, c + 1, m)
for s in range(1,33):
    for m in range(5):
        if f(s,0,m)== 1:
            print(s,m)
            break
        # 14
        # 5
        # 9, 10









# ответы 1 - 14, 2 - 5, 3 - 9 10
