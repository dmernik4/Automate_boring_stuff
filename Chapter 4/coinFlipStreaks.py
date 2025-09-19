import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # code that creates a list of 100 'heads' or 'tales' values.
    numberOfFlips = 100
    flipList = []
    tail = 0
    head = 0

    for i in range(numberOfFlips):
        flip = random.randint(0, 1)
        if flip == 0:
            flipList.append("T")
        else:
            flipList.append("H")
    print(flipList)

    # code that checks if there is a streak of 6 heads or tails in a row.
    joinedList = "".join(flipList)
    if joinedList.count("TTTTTT") == True:
        numberOfStreaks += 1
    if joinedList.count("HHHHHH") == True:
        numberOfStreaks += 1

"""
Tukaj sešteje samo za eno serijo, potrebno je sešteti vse serije skupaj!
"""
print(numberOfStreaks)
print("Chance of streak: %s%%" % ((numberOfStreaks / 10000) * 100))
