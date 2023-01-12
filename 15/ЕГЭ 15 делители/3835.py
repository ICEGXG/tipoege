#3835
k = 0
for a in range(1,1001):
    s = 0 # флаг, датчик
    for x in range(1,1001):
        if ((a %9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))) == 0:
            s = 1
    if s == 0:
        k += 1
        #print(a)
print(k)
