"""
File: stats.py
Defines three statistical functions of a given 
list of numbers: mean, median, and mode.
"""
def getMean(numbers):
    """
    getMean() accepts a list of numbers as an
    argument and returns the mean of the list.
    """
    sum = 0
    for x in numbers:
        sum += x
    return round((sum / len(numbers)), 3)

def getMedian(numbers):
    """
    getMedian() accepts a list of numbers as an
    argument and returns the median of the list.
    """
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return round((numbers[midpoint] + numbers[midpoint - 1]) / 2, 2)

def getMode(numbers):
    """
    getMode() accepts a list of numbers as an
    argument and returns the mode of the list.
    """
    if not numbers:
        return 0

    theDictionary = {}
    for x in numbers:
        number = theDictionary.get(x, None)
        if number is None:
            theDictionary[x] = 1
        else:
            theDictionary[x] += 1

    maxVal = max(theDictionary.values())

    if maxVal == 1:
        return 0

    modes = [key for key, value in theDictionary.items() if value == maxVal]
    return modes[0]

def main():
    numList = [1, 2, 3, 3, 4, 5]
    print(getMean(numList))
    print(getMedian(numList))
    print(getMode(numList))

if __name__ == "__main__":
    main()