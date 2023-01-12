# 3430
s = '5' * 400
x = len(s)
k = 0
while s.find('555') != -1 or s.find('333') != -1:
    if s.find('555') != -1:
        s = s.replace('555','3',1)
        k +=3
    else:
        s = s.replace('333','5',1)
print(k)
