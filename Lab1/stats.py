def mean(arr):
    total = 0
    for x in arr:
        total = total + x
    mean = total / len(arr)
    print(mean)

# def mode(arr):

def median(arr):
    arr.sort()
    mid = len(arr)
    median = arr[mid]
    print(median)