'''В файле содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от –10 000 до 10 000
включительно. Определите количество пар последовательности, в которых
хотя бы одно число делится на 3, а сумма элементов пары не более
максимального элемента последовательности, кратного 3. В ответе запишите
количество найденных пар, затем максимальную из сумм элементов таких
пар. В данной задаче под парой подразумевается два идущих подряд
элемента последовательности.'''
# with - менеджер контекста. позволяет открыть файлы (закрываются в автоматическом режиме)
with open('17.txt') as f:  # открыть файл 17.txt как некий объект f
    numbers = [int(x) for x in f] # преобразовать текст в целочисленный список
    s = []  # пустой список. в нем будем хранить суммы пар подходящих элементов
    print(numbers)
    for i in range(1, len(numbers)):
        if numbers[i] % 3 == 0 or numbers[i - 1] % 3 == 0:  # если условие выполняется
            # в конец списка дописываем сумму элементов
            s.append(numbers[i] + numbers[i - 1])
print(len(s))  # длина списка s - количество интересующих нас пар
print(max(s)) # вывод максимального элемента из списка s
            
