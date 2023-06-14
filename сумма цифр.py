def createList(r1, r2): 
    if (r1 == r2): 
        return r1 
    else:
        A= [] 
        while(r1 < r2+1 ):    
            A.append(r1) 
            r1 += 1
        return A
r1=273
r2=978
print(createList(r1, r2))
B=[]
s=0
for i in range(r1, r2):
    B=createList(r1, r2)
    a=i%10
    b=i%10/10
    c=i/100
    if a!=b and c!=a and b!=c:
        s=s+i
 
print("sum",s)
