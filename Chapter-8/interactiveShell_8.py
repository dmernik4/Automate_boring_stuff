# Chapter 8 "mini" programs

import pyinputplus as pyip

"""
while True:
    print("Enter you age:")
    age = input()
    try:
        age = int(age)
    except:
        print("Please use a numeric digits.")
        continue
    if age < 1:
        print("Please enter a positive number.")
        continue
    break

print(f"Your age is {age}.")

response = pyip.inputNum()
print(response)

response = pyip.inputInt(prompt="Enter a number: ")


responseMin = pyip.inputNum("Enter a number: ", min=4)
responseGT = pyip.inputNum("Enter a number: ", greaterThan=4)
responseLT = pyip.inputNum("Enter a number: ", lessThan=6)

response = pyip.inputNum("Enter num: ", blank=True)


response = pyip.inputNum(limit=2)
response = pyip.inputNum(timeout=10)
response = pyip.inputNum(limit=2, default="N/A")

response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
response = pyip.inputNum(allowRegexes=[r"(i|v|x|l|c|d|m)+", r"zero"])

response = pyip.inputNum(blockRegexes=[r"[02468]$"])

response = pyip.inputStr(
    allowRegexes=[r"caterpillar", "category"], blockRegexes=[r"cat"]
)
"""


def addUpToTen(numbers):
    numberList = list(numbers)
    for i, digit in enumerate(numberList):
        numberList[i] = int(digit)
    if sum(numberList) != 10:
        raise Exception("The digits must add up to 10, not %s." % (sum(numberList)))
    return int(numbers)  # Return int form numbers.


response = pyip.inputCustom(addUpToTen)  # No parentheses after
