#   Найти все  натуральные делители чисел из указанного диапазона.
k=1
for N in range (126849, 126872) :
  for d in range (2, N//2+1 ) :
    if N % d == 0:
      k+=1
  if k == 4:
    print(N)
  k = 0
  
      

