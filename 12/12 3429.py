# 3429
##Дана строка, состоящая из 200 цифр 5.
##Чему равна сумма цифр строки, полученной после обработки по этой программе?
s = '5' * 200
while '555' in s or '333' in s:
    if '555' in s:
        s = s.replace('555','3',1) # в скобках: что меняем, на что, сколько раз
    else:
        s = s.replace('333','5',1)  
print(s)
k = 0 
for i in range(len(s)):
    k += int(s[i])
print(k)
