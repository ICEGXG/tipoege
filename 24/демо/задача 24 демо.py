f=open('241.txt')# открыть файл 24.txt
s=f.readline() # считываем содержимое файла f в строку и записываем строку в s
k=1 # обнуляем счетчик k, будет считать количество нужных символов
kmax=0 # максимум
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        k+=1
        kmax=max(k,kmax)
    else:
        k=1
print(kmax)

