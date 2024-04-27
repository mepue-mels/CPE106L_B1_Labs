def getMode(words):
    if not words:
        return 0

    theDictionary = {}
    for word in words:
        number = theDictionary.get(word, None)
        if number is None:
            theDictionary[word] = 1
        else:
            theDictionary[word] += 1

    theMaximum = max(theDictionary.values())

    if theMaximum == 1:
        return 0

    modes = [key for key, value in theDictionary.items() if value == theMaximum]
    return modes[0]


def getMedian(numbers):
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return int((numbers[midpoint] + numbers[midpoint - 1]) / 2)


def getMean(numbers):
    sum = 0

    for x in numbers:
            sum += x

    return (sum / len(numbers))


def main():
    list_length = int(input("Enter the list length: "))
    numberList = [0] * list_length

    for i in range( list_length ):
        numberList[i] = int(input("Enter element: "))

    print("[0] Mean [1] Median [2] Mode")

    choice = int(input("Enter your choice: "))

    if (choice == 0):
        print( getMean(numberList) )
    elif (choice == 1):
        print( getMedian(numberList) )
    elif (choice == 2):
        print( getMode(numberList) )

if __name__ == "__main__":
    main()
