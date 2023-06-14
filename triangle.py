n=int(input())
tr=[]
for i in range(n+1):
    tr.append([1]+[0]*n)

for i in range(1,n+1):
    for j in range(1,i+1):
        tr[i][j]=tr[i-1][j]+tr[i-1][j-1]
        
for i in range(0,n+1):
    for j in range(0,i+1):

        print(tr[i][j],end='')
    print()
