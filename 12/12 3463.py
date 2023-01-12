# 3463
s = '>' + '1' * 20 + '2' * 15 + '3' * 40 + '<'
while s.find('><') != -1 :
    s = s.replace('>1','3>',1)
    s = s.replace('>2','2>',1)
    s = s.replace('>3','1>',1)    
    s = s.replace('3<','<1',1)    
    s = s.replace('2<','<3',1)
    s = s.replace('1<','<2',1)
s = s.replace('>','',1)
s = s.replace('<','',1)
x = int(s)
sum = 0
while x > 0:
    d = x % 10
    sum += d
    x //= 10
print(s, sum)
