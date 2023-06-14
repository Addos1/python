from random import randint
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
n=int(input())
x=[randint(0,n) for i in range(n)]
x.sort()
a=[]
for i in range (0, n, 2):
    a.append(x[i])
for i in reversed(range (0, n, 3)):
    a.append(x[i])
y_pos = np.arange(len(a))
plt.bar(y_pos, a, align='center', alpha=0.5)
plt.xticks(y_pos, a)
plt.show()
