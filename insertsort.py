from datetime import datetime
import time

start_time = datetime.now()
d=[12,4,5,6,7,3,1,15]
def ins(d):
	for i in range(len(d)):
		j=i-1
		k=d[i]
		while d[j]>k and j>=0:
			d[j+1]=d[j]
			j-=1
		d[j+1]=k
	return d
print(d)
ins(d)
print(d)
time.sleep(5)
print(datetime.now() - start_time)
print ("insert")
