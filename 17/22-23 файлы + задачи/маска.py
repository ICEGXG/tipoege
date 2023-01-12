def f(a):
    s = str(a)
    x = s[0]
    y = s[1]
    if ( '6' in s and x == '1' and y == '1'): return 1
    else: return 0   
t = 112762
print(f(t))
