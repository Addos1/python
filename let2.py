import random
n=100
k=[chr(random.randint(40,120)) for i in range(n)]
print(k)

for i in range(n-1):
    for j in range(i+1, n):
        if k[i] != k[j]:
            print("одинаковы")
            quit()
        else:
            print("одинаковы")
            quit()
