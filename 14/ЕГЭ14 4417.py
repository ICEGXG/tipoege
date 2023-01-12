a = (64 ** 25 + 4 ** 10) - (16 ** 20 + 32 ** 3)
print(a)
a1 = ''
while a > 0:
    d = str(a % 4)
    a1 = a1 + d
    a = a // 4
print(a1)
#a1 = a1[::-1]
print(a1)
for i in range(len(a1)):
    if a1[i] == '3':
        print(i)
        break
    