
htab=[None]*800

k=range(801,1601)

def ins(htab, k ):
    for i in htab:
        hk = k%len(htab)
        htab[hk] = k

for i in k:
    ins(htab, i)
    sl=dict([(i%800, i)])
    print(sl)
print(htab)

