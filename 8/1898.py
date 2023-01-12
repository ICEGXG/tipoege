##Сколько существует чисел, восьмеричная запись которых содержит 6 цифр,
##причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
k = 0
c = '0246'
n = '1357'
for i in range(100000,1000000):
    s = str(i)
    if len(set(s)) == 6:
        if ((s[0] in c and s[1] in n and s[2] in c and s[3]in n and s[4] in c and s[5]in n) or
            (s[0] in n and s[1] in c and s[2] in n and s[3]in c and s[4] in n and s[5]in c)):
            k += 1
print(k)
