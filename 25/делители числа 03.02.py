#   Найти все делители данного натурального числа N.
k = 0
N = 174459
for d in range (1, N//2+1):
       a = [0]*100
       i = 0
       if N % d == 0 and d != 1 and d != N:
               print(d)
               k+=1                    
print(N)
                     
      

