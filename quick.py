from datetime import datetime
import time

start_time = datetime.now()
a=[12,4,5,6,7,3,1,15]
def quicksort(array):
    qsort(array, 0, len(array)-1)

def qsort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        qsort(A, lo, p)
        qsort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[lo]
    i, j = lo-1, hi+1
    while True:
      i += 1
      j -= 1
      while(A[i] < pivot): i+= 1
      while(A[j] > pivot ): j-= 1

      if i >= j: 
          return j

      A[i], A[j] = A[j], A[i]
print(a)
quicksort(a)
print(a)
time.sleep(5)
print(datetime.now() - start_time)
print ("quick")
