from random import shuffle
k=[chr (x) for x in range (ord('A'), ord('Z'))]+[chr(y) for y in range(ord('a'), ord('z'))]
shuffle(k)
import random
arr=[]
for i in range(30):
    r=random.randint(1,3)
    if r==1: arr.append(k[random.randint(0,len(k)-1)])
    elif r==2: arr.append(k[random.randint(0,len(k)-1)]+k[random.randint(0,len(k)-1)])
    else: arr.append(k[random.randint(0,len(k)-1)]+k[random.randint(0,len(k)-1)]+k[random.randint(0,len(k)-1)])
print(arr)
num=[]
sum=0
for i in arr:
    if len(i)==1:num.append(ord(i))
    else:
        i=list(i)
        for q in i:
            q=ord(q)
            sum=sum+q
        num.append(sum)
print(num)

sr=0
if num.index(min(num))< num.index(max(num)):
    z=num[num.index(min(num)):  num.index(max(num))]
    for i in z:
        sr=sr+i
    sr=sr+max(num)
else:
    z=num[num.index(min(num)):num.index(max(num))]
    for i in z:
        sr=sr+i
    sr=sr+min(num)
print(z)
print(sr)

def to_matrix(num,n):
    return[num[i:i+n] for i in range(0, len(num), n)]
mas=to_matrix(num, 5)
print(mas)
l=[[row[i] for row in mas] for i in [0, 1, 2, 3, 4]]
mas=[j for sub in l for j in sub]
print(mas)

sl=0
if mas.index(min(mas))< mas.index(max(mas)):
    z=mas[mas.index(min(mas)):  mas.index(max(mas))]
    for i in z:
        sl=sl+i
    sl=sl+max(num)
else:
    z=mas[mas.index(min(mas)):mas.index(max(mas))]
    for i in z:
        sl=sl+i
    sl=sl+min(num)
print(z)
print(sl)

if sr>sl: outs=sr-sl
else: outs=sl-sr
print(outs)
al=0
for i in num: al=al+i
ins=al-outs
print(ins)
