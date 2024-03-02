import math

def mean(numList):
    length = len(numList)
    return float(sum(numList)/length)

def median(numList):
    length = len(numList)
    # for odd list count = one median
    if length % 2 == 1: 
        return(numList[int((length + 1)/2)])
    # for even list count = average of medians
    else:
        min = int(length/2)
        max = int((length/2)+1)
        return((numList[min]+numList[max])/2)


def mode():
    pass

def main():
    myList = [18, 19, 19, 19, 20, 23, 25, 26]
    # myList2 = [73, 80, 82, 93, 83, 83, 86, 90, 90, 89, 75, 82, 94, 82, 82, 84, 85, 82]
    print("Length of list:", len(myList))
    print("Mean:", mean(myList))
    print("Median:", median(myList))
    # print("Mode:", mode(myList))

if __name__ == "__main__":
    main()