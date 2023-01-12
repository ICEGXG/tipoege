#3084
def f(s,c,m):
    if 43 <= s <= 72:
        return c % 2 == m % 2 # выигрываем мы == наш ход
    if s > 72:
        return  c % 2 != m % 2 # условие проигрыша противника != ход противника
    if c == m:
        return 0
    if (c + 1) % 2 == m % 2:
        return f(s + 1, c + 1, m) or f(s * 2, c + 1, m) or f(s * 3, c + 1, m)
    else:
        # для задачи 4109 если выигрыш после неудачного хода противника, то
        # в ветке else меняем and на or!
        # для остальных случаев мы не меняем
        return f(s + 1, c + 1, m) and f(s * 2, c + 1, m) and f(s * 3, c + 1, m)
for s in range(1, 44):
    for m in range(1,5):
        if f(s,0,m) == 1:
            print(s,m)
            break
        
# самостоятельно №№ 3083, 3082, 4109


