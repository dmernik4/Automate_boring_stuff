import pyperclip

"""
spam = "Say hi to Bob's mother."
print(spam)


print("Hello there!\nHow are you?\nI'm doing fine.")


print(
    '''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob'''
)


spam = "Hello, world!"
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[7:])

fizz = spam[0:5]
print(fizz)


name = "Al"
age = 4000
print("Hello, my name is " + name + ". I'm " + str(age) + " years old.")
print(("Hello, my name is %s. I'm %s years old.") % (name, age))
print(f"Hello, my name is {name}. I'm {age} years old.")
print(f"Hello, my name is {name}. Next year I'll be {age + 1}.")


spam = "Hello, world!"
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)


spam = ["cats", "rats", "bats"]
print((", ".join(spam)))
bacon = ["My", "name", "is", "Simon"]
print((" ".join(bacon)))
print(("ABC".join(bacon)))


spam = "My name is Simon"
print(spam.split())
bacon = "MyABCnameABCisABCSimon"
print(bacon.split("ABC"))
print(spam.split("m"))


spam = '''Dear Alice,
How have you been? I'm fine.
There is a container in the fridge
that is labeled "Milk experiment."

Please do not drink it.
Sincerely,
Bob'''

print(spam.split("\n"))

spam = "Hello, world!"
print(spam.partition("w"))
print(spam.partition("world"))
print(spam.partition("o"))
print(spam.partition("XYZ"))


spam = "Hello"
bacon = "Hello, world!"
print(spam.rjust(10))
print(spam.rjust(20))
print(bacon.rjust(20))
print(spam.ljust(10))
print(spam.rjust(20, "*"))
print(spam.rjust(20, "-"))
print(spam.center(20))
print(spam.center(20, "="))


spam = "    Hello, World    "
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

bacon = "SpamSpamBaconSpamEggsSpamSpam"
print(bacon.strip("ampS"))

print(ord("A"))
print(ord("4"))
print(ord("!"))
print(chr(65))
"""

pyperclip.copy("Hello, world!")
pyperclip.paste()
