import math
beg=0
step=0.1
end=1
while step>0.00001:
    while beg<=end:
        beg=beg+step
        if (math.cos(4*beg)<0 and math.cos(4*(beg-step))>0) or (math.cos(4*beg)>0 and math.cos(4*(beg-step))<0):
            step=step/10
            break
print(beg)
