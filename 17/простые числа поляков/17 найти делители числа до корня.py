k=0 # считает количество делителей
m=0 # считает количство нужных чисел
n=int(input('введите число '))
for d in range (1,n//2+1):
    if n % d == 0:
        k+=1
        print(d)
print(k)
