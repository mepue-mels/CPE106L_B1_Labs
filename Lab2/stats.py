#!/usr/bin/env python3
def getMode():
        fileName = input("Enter the file name: ")
        f = open(fileName, 'r')

        words = []
        for line in f:
            wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())

        theDictionary = {}
        for word in words:
            number = theDictionary.get(word, None)
        if number == None:
            theDictionary[word] = 1
        else:
            theDictionary[word] = number + 1

        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key
                break
            else:
                return 0

def getMedian():
    fileName = input("Enter the file name: ")
    f = open(fileName, 'r')

    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

        numbers.sort()
        midpoint = len(numbers) // 2
        print("The median is", end=" ")
        if len(numbers) % 2 == 1:
            return numbers[midpoint]
        else:
            return ((numbers[midpoint] + numbers[midpoint - 1]) / 2)

def getMean():
    fileName = input("Enter the file name: ")
    f = open(fileName, 'r')

    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

    length = len(numbers)
    sum = 0

    for x in numbers:
        sum += x

    return ( sum / length )
