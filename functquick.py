a=[65,23,76,24,98,13,46,36,21,56,34,41,86,51,23,38,67,15,22,58]
def quicksortBetter(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortBetter(left) + middle + quicksortBetter(right)
print(a)
quicksortBetter(a)
print(a)
