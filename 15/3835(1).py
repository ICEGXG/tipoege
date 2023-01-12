k = 0 # счетчик
for a in range(1,1001):
    s = 0
    for x in range(1,10000):
        if ((a % 9 == 0) and ((280 % x == 0) <=((a % x != 0) <= (730%x != 0)))) == 0:
            s = 1
    if s == 0:
        #print(a)
        k += 1
print(k)
            
