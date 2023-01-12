f=open('241.txt')# открыть файл 24.txt
s=f.read() # считываем содержимое файла f в строку и записываем строку в s
ka=0 # обнуляем счетчик k, будет считать количество нужных символов
ke=0 # максимум
x=0
for i in range(len(s)):
    if s[i]!='\n':
        if s[i]=='A':
            ka+=1
        if s[i]=='E':
            ke+=1          
    else:
        if ka>ke:
            x+=1
        ka=0
        ke=0 
print(ka,ke,x)

