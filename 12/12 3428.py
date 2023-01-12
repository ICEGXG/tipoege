#  12   3428 
s = '5' * 300
while s.find ('555') != -1 or s.find('333') != -1:
    if s.find ('555') != -1:
        s = s.replace('555','3',1)
    else:
        s = s.replace('333','5',1)
k = s.count('5')
print(k,s,sep = '\n')
