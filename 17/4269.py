'''(№ 4269) (В. Шубинкин) В файле 17-1.txt содержится последовательность
целых чисел. Элементы последовательности могут принимать целые значения
от -10 000 до 10 000 включительно.
Определите и запишите в ответе
сначала количество пар элементов последовательности,
в которых хотя бы одно число делится на 7,
а другое при этом не делится на 17.
Затем - минимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих
подряд элемента последовательности. Например,
для последовательности -45; 14; 22; -21; 34
ответом будет пара чисел: 3 и -31.'''
with open('17-1.txt') as f: # открыть файл 17-1.txt и записать как некий объект f
    s = [int(x) for x in f] # создаем список из чисел
print(s[:10])
s1 = [] # пустой массив, в который запишем суммы элементов
for i in range(len(s)-1):
    if ((s[i] % 7 == 0 and s[i+1] % 17 != 0) or (s[i] % 17 != 0 and s[i+1] % 7 == 0)):
        s1.append(s[i]+ s[i+1])
print(s1[:10])
print(len(s1))
print(min(s1))









    



