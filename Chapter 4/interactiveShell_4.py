"""
spam = ["cat", "bat", "rat", "elephant"]
print("Hello, " + spam[0])
print("The " + spam[1] + " and the " + spam[0])
print(spam[-1])
print("The " + spam[-1] + " is afraid of the " + spam[-3])

spam = ["cat", "bat", "rat", "elephant"]
print(spam[0:4])
print(spam[1:3])
print(spam[0:-3])
print(spam[:2])
print(spam[1:])
print(spam[:])

spam = ["cat", "dog", "mouse"]
print(len(spam))

spam1 = ["cat", "bat", "rat", "elephant"]
spam1[1] = "aardvark"
spam1[2] = spam1[1]
spam1[-1] = 12345
print(spam1)

spam1 = [1, 2, 3]
spam2 = ["a", "b", "c"]
print(spam1 + spam2)
print(spam2 * 3)

spam = ["cat", "bat", "rat", "elephant"]
del spam[2]
print(spam)

supplies = ["penns", "staplers", "flamethrowers", "binders"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

"howdy" in ["hello", "hi", "howdy", "heyas"]

supplies = ["penns", "staplers", "flamethrowers", "binders"]
for index, item in enumerate(supplies):
    print("Index " + str(index) + " in supplies is: " + item)

import random

pets = ["Dog", "Cat", "Moose"]
print(random.choice(pets))

people = ["Alice", "Bob", "Carol", "David"]
random.shuffle(people)
print(people)

spam = "Hello,"
spam += " world!"
print(spam)
bacon = ["Zophie"]
bacon *= 3
print(bacon)

spam = ["hello", "hi", "howdy", "heyas"]
print(spam.index("hello"))
print(spam.index("heyas"))

myPets = ["Zophie", "Pooka", "Fat-tail", "Pooka"]
print(myPets.index("Pooka"))

spam = ["cat", "bat", "rat"]
spam.append("moose")
print(spam)
spam.insert(1, "chicken")
print(spam)

spam = ["cat", "bat", "rat", "elephant", "bat"]
spam.remove("bat")
print(spam)

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spamName = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
spamName.sort()
print(spamName)

spamLower = ["a", "z", "A", "Z"]
spamLower.sort(key=str.lower)
print(spamLower)

spamReverse = ["cat", "dog", "moose"]
spamReverse.reverse()
print(spamReverse)

name = "Zophie"
print(name[0])
print(name[-2])
print(name[0:4])
print(name[0])
for i in name:
    print("* * * " + i + " * * *")

name = "Zophie a cat"
newName = name[0:7] + "the" + name[8:12]
print(newName)

eggs = ("hello", 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

print(type(("hello",)))
print(type(("hello")))

tuple(["cat", "dog", 5])
print(tuple)
print(lists(("cat", "dog", 5)))

list("hello")
print(list)

spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # The reference is being copied, not the list
cheese[1] = "Hello"  # This changes the list value
print(spam)
print(cheese)  # The cheese variable refers to the same list

print(id("Howdy"))
bacon = "Hello"
print(id(bacon))
bacon += " world!"
print(id(bacon))

eggs = ["cat", "dog"]  # This creates a new list
print(id(eggs))
eggs.append("moose")  # append() modifies the list "in place"
print(id(eggs))  # Eggs still refers to the same list as before
eggs = ["bat", "rat", "cow"]  # This creates a new list, witch has a new id
print(id(eggs))  # Eggs now refer to a completely new list
"""

import copy

spam = ["A", "B", "C", "D"]
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese))  # cheese is a different list with different id
cheese[1] = 42
print(spam)
print(cheese)
