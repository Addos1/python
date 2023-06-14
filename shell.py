from datetime import datetime
import time

start_time = datetime.now()
b=[12,4,5,6,7,3,1,15]
def shell(a):
    g=len(a)//2
    while g>0:
        for i in range(g, len(a)):
            x=a[i]
            j=i
            while j>=g and x<=a[j-g]:
                a[j]=a[j-g]
                j=j-g
            a[j]=x
        g=g//2
print(b)
shell(b)
print(b)
time.sleep(5)
print(datetime.now() - start_time)
print("shell")

from random import randint
n=int(input())
x=[randint(0,n) for i in range(n)]
x.sort()
a=[]
for i in range (0, n, 2):
    a.append(x[i])
for i in reversed(range (0, n, 3)):
    a.append(x[i])
print(a)
