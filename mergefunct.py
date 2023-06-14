from datetime import datetime
import time
start_time = datetime.now()
a=[65,23,76,24,98,13,46,36,21,56,34,41,86,51,23,38,67,15,22,58]
def mergesort(a):
    if len(a) > 1:
        lt, rt = map(lambda l: list(reversed(mergesort(l))), (a[::2], a[1::2]))
        a.clear()
        while lt and rt:
            a.append(lt.pop() if lt[-1] < rt[-1] else rt.pop())
        a.extend(lt[::-1])
        a.extend(rt[::-1])
    return a
print(a)
mergesort(a)
print(a)
time.sleep(5)
print(datetime.now() - start_time)
print("merge")
