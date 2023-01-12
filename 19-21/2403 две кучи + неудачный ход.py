# 2403 две кучи +2 *2 a = 7  1 <=b<=66 a+b >=74

def f(a,b,c,m):
    if a+b >= 74: return c%2 == m%2
    if c == m: return 0
    if (c + 1) % 2 == m % 2:
        return f(a+2,b,c+1,m) or f(a,b+2,c+1,m) or f(a*2,b,c+1,m) or f(a,b*2,c+1,m)
    else:
        # если у нас неудачный ход одного из игроков то в ветке else меняем и на или
        # ветку if не трогаем!
        return f(a+2,b,c+1,m) and f(a,b+2,c+1,m) and f(a*2,b,c+1,m) and f(a,b*2,c+1,m)
for b in range(1,67):
    for m in range(1,5):
        if f(7,b,0,m) == 1:
            print(b,m)
            break
# 17   29       27 30
