from datetime import datetime
import time

start_time = datetime.now()

a=[12,4,5,6,7,3,1,15]
def merge(a):
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]
        merge(l)
        merge(r)
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i=i+1
                k=k+1
            else:
                a[k]=r[j]
                j=j+1
                k=k+1
        while len(l)>i:
            a[k]=l[i]
            i=i+1
            k=k+1
        while len(r)>j:
            a[k]=r[j]
            j=j+1
            k=k+1
print(a)
merge(a)
print(a)
time.sleep(5)
print(datetime.now() - start_time)
print("merge")
from datetime import datetime
import time
start_time = datetime.now()
a=[12,4,5,6,7,3,1,15]
def mergesort(a):
    if len(a) > 1:
        lt, rt = map(lambda l: list(reversed(mergesort(l))), (a[::2], a[1::2]))
        a.clear()
        while lt and rt:
            a.append(lt.pop() if lt[-1] < rt[-1] else rt.pop())
        a.extend(lt[::-1])
        a.extend(rt[::-1])
    return a
mergesort(a)
print(a)
time.sleep(5)
print(datetime.now() - start_time)
print("merge")
