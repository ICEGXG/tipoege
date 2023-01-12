k = 0
#   Найти все  натуральные делители чисел из указанного диапазона.
for N in range (150750, 150765) :
  for d in range (1, N//2+1 ) :
    if N % d == 0: 
      k+=1
  if k == 4:
    print(N)
  k = 0

  

        
      #print (d, ' ', sep = '', end = '')
      

