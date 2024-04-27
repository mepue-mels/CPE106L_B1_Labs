def readLine(file_path, line_num):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        if (line_num >= 1 and line_num <= len(lines)):
            print(lines[line_num - 1])
        else:
            print("Out of bounds.")


file_path = input("Enter file name in directory: ")

line_num = input("Enter line number: ")

readLine(file_path, int(line_num))
