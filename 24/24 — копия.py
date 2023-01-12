f=open('241.txt')
s=f.readline()
sm=1
smax=0
for i in range (0,len(s)-1):
    if int(s[i])+int(s[i+1])>=10:
        sm+=1
        if sm>=smax:
            smax=sm
    else:
        sm=1
print(smax)
