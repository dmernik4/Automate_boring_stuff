"""import sys


def collatz(num):
    num = int(num)
    while True:
        if num % 2 == 0:
            result = num // 2
            if result == 1:
                print(result)
                print("You have reached number 1!")
                sys.exit()
            else:
                print(result)

        elif (num % 2) == 1:
            result = 3 * num + 1
            if result == 1:
                print(result)
                print("You have reached number 1!")
                sys.exit()
            else:
                print(result)
        num = result


try:
    print("Enter a number:")
    num = input()
    collatz(num)

except ValueError:
    print("You did not enter a number.")
"""


def collatz(num):

    while num > 1:
        num = int(num)
        print(num)
        if num % 2 != 0:
            num = 3 * num + 1
        else:
            num = num / 2
    num = int(num)
    print(num)


try:
    print("Enter the number:")
    num = int(input())
    collatz(num)
except ValueError:
    print("Enter a valid number!")
