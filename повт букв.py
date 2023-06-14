import random
n=100
k=[chr(random.randint(40,120)) for i in range(n)]
print(k)
chars =[chr(i) for i in range(80)]

for char in chars:
  count = k.count(char)
  if count > 1:
    print (char, count)
