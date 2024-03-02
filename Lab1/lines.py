def printLine():
    file = open("cat.txt", "r")
    print('Input line number: ')
    x = int(input())
    if x <= 0:
        print("Invalid line.")
    else:
        line = file.readlines()[x-1]
        print(line)

printLine()