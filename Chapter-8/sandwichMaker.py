import pyinputplus as pyip


prices = {
    "bread": {"wheat": 3, "white": 2, "sourdough": 4},
    "protein": {"chicken": 2, "turkey": 2, "ham": 2, "tofu": 2},
    "cheese": {"cheddar": 1, "swiss": 1, "mozzarella": 1},
    "extra": {"mayo": 1, "lettuce": 1, "mustard": 1, "tomato": 1},
}

promptBread = "What type of bread would you like:\n"
promptProtein = "What type of protein would you like:\n"
promptCheeseYN = "Would you like some cheese (yes/no): "
promptCheeseType = "What kind of cheese would you like:\n"
promptMayo = "Would you like some mayo (yes/no): "
promptLettuce = "Would you like some lettuce (yes/no): "
promptMustard = "Would you like some mustard (yes/no): "
promptTomato = "Would you like some tomato (yes/no): "
promptQuantity = "How many sandwiches would you like: "


responseBread = pyip.inputMenu([r"wheat", "white", "sourdough"], promptBread)
responseProtein = pyip.inputMenu([r"chicken", "turkey", "ham", "tofu"], promptProtein)
responseCheeseYN = pyip.inputYesNo(promptCheeseYN)
if responseCheeseYN == "yes":
    responseCheese = pyip.inputMenu(
        [r"cheddar", "swiss", "mozzarella"], promptCheeseType
    )
else:
    responseCheese = False

responseMayo = pyip.inputYesNo(promptMayo)
responseLettuce = pyip.inputYesNo(promptLettuce)
responseMustard = pyip.inputYesNo(promptMustard)
responseTomato = pyip.inputYesNo(promptTomato)
responseQuantity = pyip.inputNum(promptQuantity, min=1)


totalAmount = 0
totalAmount += prices["bread"][responseBread]
totalAmount += prices["protein"][responseProtein]

if responseCheese:
    totalAmount += prices["cheese"][responseCheese]
if responseMayo == "yes":
    totalAmount += prices["extra"]["mayo"]
if responseLettuce == "yes":
    totalAmount += prices["extra"]["lettuce"]
if responseMustard == "yes":
    totalAmount += prices["extra"]["mustard"]
if responseTomato == "yes":
    totalAmount += prices["extra"]["tomato"]

totalAmount *= responseQuantity


print("\n--------------------\n")
if responseQuantity == 1:
    print(
        f"You have ordered {responseQuantity} sandwich with {responseBread} bread and {responseProtein}."
    )
else:
    print(
        f"You have ordered {responseQuantity} sandwiches with {responseBread} bread and {responseProtein}."
    )
print("You also ordered some extras:")
if responseCheeseYN == "yes":
    print(f"\t- {responseCheese} cheese")
if responseMayo == "yes":
    print(f"\t- mayo")
if responseLettuce == "yes":
    print(f"\t- lettuce")
if responseMustard == "yes":
    print(f"\t- mustard")
if responseTomato == "yes":
    print(f"\t- tomato")
print("\n--------------------\n")
print(f"Your total amount is: {totalAmount}€.")
print("Thank you! Come back soon!")
