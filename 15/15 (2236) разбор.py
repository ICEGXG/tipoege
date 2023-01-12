k = 0
amax = 0
for a in range(1, 1000):
    s = 0
    for x in range(1, 1000):
        if ((x % a == 0) or (x % 6 != 0) or (x % 9 != 0)) == False:
            s = 1
    if s == 0:
        print(a)
        k += 1
        amax = max(a, amax)
print('***')
print(amax)
print(k)

