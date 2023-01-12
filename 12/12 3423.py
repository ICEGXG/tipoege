#3423
s = '4' + '6' * 79 + '4'
print(s)
while s.find('63') != -1 or s.find('664') != -1 or s.find('6665') != -1:
    if s.find('63') != -1:
        s = s.replace('63','4',1)
    elif s.find('664') != -1:
        s = s.replace('664','5',1)
    elif s.find('6665') != -1:
        s = s.replace('6665','3',1)
print('***',s)
