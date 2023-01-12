for a in range (1,1000):
    s=0
    for x in range (1,10000):
        if ((x%a==0) or not(x%6==0) or not(x%9==0))==0:
            s=1
    if s==0:
        print(a)
print('end')
    
