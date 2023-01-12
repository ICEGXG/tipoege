'''(№ 4722) В файле 17-243.txt содержится последовательность целых чисел. 
Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно. 
Определите количество пар чисел, в которых ровно один из двух элементов больше, 
чем сумма цифр всех чисел в файле, делящихся на 35, а шестнадцатеричная запись другого оканчивается на EF. 
В ответе запишите два числа: сначала количество найденных пар, 
а затем – минимальную сумму элементов таких пар. 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.'''
with open('17.txt') as f:  # открыть файл 17 и преобразовать в объект f
    # составляем список из символов файла, преобразовываем каждый элемент в целый тип
    num = [int(x) for x in f]
    sn = 0 # сумма всех элементов массива
    s = []  # пустой список, где будут храниться нужные пары
    print(num)
    for x in num:
        if x % 35 == 0:
            sn += x
print(sn)
