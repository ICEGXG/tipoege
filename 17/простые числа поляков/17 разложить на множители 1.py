k1 = 0
x=int(input("* "))
while x !=0:
    k = 0
    y = x
    for i in range(2, y):
        if y % i == 0:
            k += 1
            print(k)
    if k == 0:
        print(k)
        k1 += 1
        print(k1)
    x=int(input("* "))
print(k1)
