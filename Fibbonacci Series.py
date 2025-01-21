fibbo=[]
n=20
a=-1
b=1
while n!=0:
    c=a+b
    fibbo.append(c)
    a=b
    b=c
    n-=1
print(fibbo)