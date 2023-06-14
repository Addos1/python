n=int(input())
for n in range(2, n+1): 
     for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            print(n, 'равно', x, '*', n//x)
            break
     else:
             print(n, '- простое число')
