import math

BinarySearch(arr, x):
    m = math.ceil(arr.length / 2)
    n = m
    while arr[m] != x and math.ceil(n/2) >= 1:
        if arr[m] < x:
            m = m + math.ceil(n/2)
        else:
            m = m - math.ceil(n/2)
        n = math.ceil(n/2)
    if arr[m] = x:
        return True
    else: return False

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(BinarySearch(arr, 6))
