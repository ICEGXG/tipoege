##Сколько существует чисел, делящихся на 5, десятичная запись которых содержит 6 цифр,
##причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
k = 0
ch = '02468'
nch = '13579'
for i in range(100000,1000000):
    s = str(i)
    if i % 5 == 0 and len(set(s)) == 6:
        if ((s[0] in ch and s[1] in nch and s[2] in ch and s[3]in nch and s[4] in ch and s[5]in nch) or
            (s[0] in nch and s[1] in ch and s[2] in nch and s[3]in ch and s[4] in nch and s[5]in ch)):
            k += 1

print(k)
# приер числа 125083 или 472945
# set(s) множество символов строки s, в нем нет одинаковых символов
