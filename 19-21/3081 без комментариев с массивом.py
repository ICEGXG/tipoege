def f(s, c, m):
    if s >= 65:
        return c % 2 == m % 2  
    if c == m: 
        return 0
    h = [f(s + 1, c + 1, m),f(s + 2, c + 1, m),f(s * 3, c + 1, m)]
    # все ходы записываем в массив
    if (c + 1) % 2 == m % 2: 
        return any(h) # большое ИЛИ
    else:  
        return all(h) # большое И
for s in range(1, 65):
    for m in range(1, 5):
        if f(s, 0, m) == 1:
            print(s, m)
            break


    
