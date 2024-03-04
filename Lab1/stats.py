import math

def mean(numList):
    return sum(numList)/len(numList)

def median(numList):
    length = len(numList)
    i = length // 2
    # for odd list count = one median
    if length % 2 == 1: 
        return(numList[i])
    # for even list count = average of medians
    return(sum(numList[i - 1: i + 1])/2)

def mode(numList):
    numCount = {}
    for i in numList:
        if not i in numCount:
            numCount[i] = 1
        else:
            numCount[i] += 1
    modeList = [x for x,y in numCount.items() if y == max(numCount.values())]
    if len(modeList) != 1:
        return "No mode."
    return modeList

def main():
    # myList = [18, 19, 19, 19, 20, 23, 25, 26]
    # get user input
    myList = input("Enter your list, separated by space: ")
    myList = myList.split(" ")
    myList = [int(x) for x in myList]

    # call functions
    print("Length of list:", len(myList))
    myList.sort()
    print("Mean:", mean(myList))
    print("Median:", median(myList))
    print("Mode:", str(mode(myList))[1:-1])

if __name__ == "__main__":
    main()