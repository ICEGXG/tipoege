'''(№ 3830) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа A формула
ДЕЛ(A, 7) ∧ (ДЕЛ(240, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(780, x)))

тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?'''
for a in range(1, 1000):
    s = 0
    for x in range(1, 1000):
        if ((a % 7 == 0) and ((240 % x != 0) or (a % x == 0) or (780 % x != 0))) == False:
            s = 1
    if s == 0:
        print(a)