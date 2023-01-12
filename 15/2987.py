'''(№ 2987) (В.Н. Шубинкин) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа A формула
(¬ДЕЛ(x, A) ∨ ДЕЛ(x, 36) ∧ ДЕЛ(x, 126)) ∧ (A > 1000)
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?'''
for a in range(1, 2000):
    s = 0
    for x in range(1, 10000):
        if ((x % a != 0) or (x % 36 == 0) and (x % 126 == 0) and (a > 1000)) == False:
            s = 3
    if s == 0:
        print(a)