# 412 Поляков
for x in range(10000,100000): # перебираем все пятизначные числа
    a = 0 
    b = 0
    y = 1
    z = x # Делаем замену переменной, т.к. она изменит свое значение на ноль
    while z > 0:            # здесь
      if (z % 10) % 2 == 0: # здесь
        a = a*10 + z % 10   # здесь
      else:
        y = y*10 
        b = b*10 + z % 10   # здесь
      z = z // 10           # здесь 
    a = a*y + b
    if a == 26391: # делаем стоп при условии
        break
print(a,x)


