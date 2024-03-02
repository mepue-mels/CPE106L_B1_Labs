import math

arr = [12, 3, 42, 5, 6, 75, 61, 23, 84, 53, 90, 71, 16, 5, 6, 12, 61, 23, 3, 6]

def mean(arr):
    total = 0
    for x in arr:
        total = total + x
    mean = total / len(arr)
    print('Mean:\t', mean)

def mode(arr):
    mode = max(arr, key = arr.count)
    print('Mode:\t', mode)

def median(arr):
    arr.sort()
    mid = len(arr) / 2
    mid = int(math.ceil(mid))
    median = arr[mid]
    print('Median:\t', median)

mean(arr)
mode(arr)
median(arr)