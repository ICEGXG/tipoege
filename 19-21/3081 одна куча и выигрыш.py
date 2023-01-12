# ПРОГРАММА ИЩЕТ ВЫИГРЫШНУЮ СТРАТЕГИЮ
# арумены функции s -количество камней, c - количество ходов, выполненных в процессе игры
# m - выигрышная позиция по условию задачи
# можно ли выиграть за m ходов?
# нечетный ход Петя, четный ход Ваня
def f(s, c, m):

    # если игра окончена, то количество ходов с должно иметь ту же четность, что и m
    if s >= 65:
        return c % 2 == m % 2  # проверка: ход Пети (нечётный) или Вани (чётный)


    # если игра не окончена за m ходов, то количество ходов должно иметь ту же четность, что и m
    if c == m: 
        return 0 # это не наша стратегия, игра закончится


    # если это ход целевого игрока, то победа в одном из вариантов
    if (c + 1) % 2 == m % 2: 
        return f(s + 1, c + 1, m) or f(s + 2, c + 1, m) or f(s * 3, c + 1, m)

    # иначе, победа должна быть во всех вариантах т.е. мы должны побеждать при любом ходе противника
    # выигрыш при любом ходе возврат функций +1 или +2 или *3
    else:  # если условие не
        return f(s + 1, c + 1, m) and f(s + 2, c + 1, m) and f(s * 3, c + 1, m)


for s in range(1, 65):
    for m in range(1, 8):
        if f(s, 0, m) == 1: # можно ли выиграть за m ходов?
          if m == 3:  # четный ход Ваня или нечетный Петя
            # можно сделать дополнительное условие, чтобы сократить вывод
            print(s, m)
            break # обязательно, иначе программа покажет лишние варианты


    
