import math

# arr = [12, 3, 42, 5, 6, 75, 61, 23, 84, 53, 90, 71, 16, 5, 6, 12, 61, 23, 3, 6]

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

def stats():
    print('Enter integers: ')
    print('Select mode:\n[1] Mean\n[2] Mode\n[3]Median')
    sel = input('Select mode:\n[1] Mean\n[2] Mode\n[3]Median')
    match sel:
        case "1":
            print('The mean is ', mean(arr))
        case "2":
            print('The mode is ', mode(arr))
        case "3":
            print('The median is ', median(arr))
        case _:
            print('Invalid selection')
    
stats()
# mean(arr)
# mode(arr)
# median(arr)