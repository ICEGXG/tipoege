k=0
s=0 # количество нужных чисел
i1=0 # временно значение i
maxi=0
for i in range (333666,666999+1):
    if i%17==0:
        i1=i
        while i1>0:
            d=i1%10 # последняя цифра
            if d==7:
                k+=1
            i1//=10
        if k>=2:
            s+=1
            if i>maxi:
                maxi=i
        k=0
print(maxi,s)
