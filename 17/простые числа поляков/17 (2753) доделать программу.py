# простые числа на интервале, у которых первая цифра больше последней
# [2095; 19402] количество и наибольшее оканцивающееся на 21.
k=0 # считает количество делителей
m=0 # считает количство нужных чисел
for n in range(17,42):
    for d in range (1, n//2+1) :
        if n % d == 0:
            k+=1 
    if k==1:
        m+=1
        print (n,k)
    k=0
print('end',m)


    
           
