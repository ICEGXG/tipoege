##(№ 1922) Артур составляет 5-буквенные коды перестановкой букв слова АРЕАЛ.
##При этом нельзя ставить рядом две гласные.
##Сколько различных кодов может составить Артур?
k = 0
s = 'арел'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    f = a+b+c+d+e
                    if ('аа' not in f and 'ае' not in f and 'еа' not in f and f.count('а') == 2 and
                        f.count('р') == 1 and f.count('е') == 1 and f.count('л') == 1):
                        k += 1
                        print(f)
print(k)
    
