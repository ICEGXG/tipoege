#3178
for a in range(130,0,-1):
    s = 0 # флаг, датчик
    for x in range(1,10000):
        if ((130 % a ==0) and ((x % a != 0) and (x % 38 ==0)) <=(x % 78!=0))  == 0:
            s = 1
    if s == 0:
        print(a)
        

