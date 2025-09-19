# This program says hello and asks for my name

print("Hello, world!")
print("What is your name?")  # ask for their name
myName = input()
print("iIt's good to meet you, " + myName)
print("The lenght of your name is:")
print(len(myName))
print("What is your age?")  # ask for their age
myAge = input()
print("You'll be " + str(int(myAge) + 1) + " in a year.")
