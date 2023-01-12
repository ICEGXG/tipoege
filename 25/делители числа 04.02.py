for N in range (174457, 174470+1):
       k = 0
       for d in range (1, N**0.5):
              if N % d == 0 and d != 1 and d != N:
                     print(d)
                     k+=1
              if k > 1 and k < 3:
                     print(N)
                     k = 0

