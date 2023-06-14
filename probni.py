


n=int(input())
a=[int(input()) for i in range(n)]
for i in range(n):
    if a[i]!=0:
        a.append(0)
        for i in range (n+1):
            x=a[i]
            k=a[i+1]-1
            if (x==k+1):
                for i in range (n):
                    a[i]=a[i]-x
                    a[i+1]=a[i+1]-k
                print(a)
                print(i+1)
            else:
                for j in range (n):
                    a[j]=a[j]-x
                print(a)
                print(j+1)
    print(j+i+2)
