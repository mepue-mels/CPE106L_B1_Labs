def mean(arr):
    sum = 0
    length = len(arr)

    for elem in arr:
        sum += elem

    return (sum / length)

def mode(arr):
    unique_elements = set(arr)
    counts = {}

    for elem in unique_elements:
        counts[elem] = arr.count(elem)

    mode_element = max(counts, key=counts.get)
    return mode_element

def median(arr):
    arr.sort()
    length = len(arr)
    return arr[int(length/2)]
