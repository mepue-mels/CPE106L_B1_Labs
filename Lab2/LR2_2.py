def readLine(file_path, line_num):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        if (line_num >= 1 and line_num <= len(lines)):
            print(lines[line_num - 1].rstrip())
        else:
            print("Out of bounds.")


def main():
    file_path = input("Enter file name in directory: ")
    line_num = int(input("Enter line number: "))

    if line_num == 0:
        print("Program exiting...")
        return
    else:
        readLine(file_path, line_num)

if __name__ == "__main__":
    main()
