import random

def main():
    print("A simple high-low program.")
    targetNumber = random.randint(1, 50)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Enter a number from 1 to 50: "))
        if userNumber < targetNumber:
            print("Too small, try again.")
        elif userNumber > targetNumber:
            print("Too large, try again.")
        else:
            print("You've guessed the number in", count, "tries!")
            break

if __name__ == "__main__":
    main()