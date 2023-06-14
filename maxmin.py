from datetime import datetime
import time

start_time = datetime.now()
n=[12,4,5,6,7,3,1,15]
def p(n, l, h):

    pvi =l
    for i in range(l+1, h+1):
        if n[i] <= n[l]:
            pvi += 1
            n[i], n[pvi] = n[pvi], n[i]
    n[pvi], n[l] = n[l], n[pvi]
    return pvi

def sr(n, l, h):
    if l >= h:
        return
    pvi = p(n, l, h)
    sr(n, l, h-1)
    sr(n, l+1, h)

def s(n, l=0, h=None):
    if h is None:
        h = len(n) - 1 
    return sr(n, l, h)
print(n)
s(n)
print(n)
time.sleep(5)
print(datetime.now() - start_time)
print ("maxmin")
