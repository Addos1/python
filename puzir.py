from datetime import datetime
import time

start_time = datetime.now()
d=[12,4,5,6,7,3,1,15]
n=len(d)
print(d)
for i in range(n-1):
    for j in range(n-i-1):
        if d[j] > d[j+1]:
            d[j], d[j+1] = d[j+1], d[j]
print(d)
time.sleep(5)
print(datetime.now() - start_time)
print ("puzir")
