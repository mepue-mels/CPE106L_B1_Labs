def main():
    userFile = str(input("Enter file name: "))
    userList = open(userFile, 'r').readlines()
    
    while 1:
        x = int(input("Select line to print, or type '0' to exit: "))
        if x == 0:
            break
        elif x - 1 < len(userList):
            print(userList[x - 1])
        else:
            print("Out of range. Please try again.")


if __name__ == "__main__":
    main()