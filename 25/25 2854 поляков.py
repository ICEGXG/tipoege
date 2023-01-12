#for x in range (298435, 363250):
a = [0]*2
k1 = 0
for x in range (298435, 363250):
    k = 0
    for i in range(2, x//2+1):
        if(x%i==0):
            k += 1
            a.append(i)
            if k == 2:
                break

        print(a)
        #k1 += 1
        #print(x)
   # k = 0
#print(k1)
