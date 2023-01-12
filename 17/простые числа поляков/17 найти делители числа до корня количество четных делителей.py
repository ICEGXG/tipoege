k=0 # считает количество делителей
m=0 # считает количство нужных чисел
n1 = int(input())
for n in range(1,n1+1):
    k = 0
    for d in range (1,n+1):
        if n % d == 0:
            k+=1
    if k % 2 ==0:
        m+=1
        #print(n)
print(m)
