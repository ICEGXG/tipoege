k = 0
s =''
w = ['оу','уо','кл','лк','нл','лн','нк','кн']
for a in 'колун':
    for b in 'колун':
        for c in 'колун':
            for d in 'колун':
                for e in 'колун':
                    if a != b != c != d != e:
                        s = a+b+c+d+e
                        print(s)
##                        fg = 0
##                        for i in range(len(s)):
##                            if w[i] in s:
##                                flag = 1
##                        if fg == 0:
##                            print(s)
##                            k += 1
##print(k)
    
