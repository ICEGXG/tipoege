a=2*10**10
b=4*10**10+1
k=0
imin=b # максимально возможное первоначальное значение
for i in range(2*10**10,4*10**10+1,100000):
    if i%7==0 and i%13!=0 and i%29!=0 and i%43!=0 and i%101!=0:
        k+=1
        if i<imin:
            imin=i
print(k,imin)
    
