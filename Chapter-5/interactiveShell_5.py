"""
myCat = {"size": "fat", "color": "gray", "disposition": "loud"}
print(myCat["size"])
print("My cat has " + myCat["color"] + " fur.")


spam = {"color": "red", "age": "42"}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
print(v, k, i)

print(spam.keys())
print(list(spam.keys()))

for k, v in spam.items():
    print("Key: " + k + ", Value: " + str(v))


spam = {"name": "Zophie", "age": 7}
if "name" in spam.keys():
    print("True")
if "Zophie" in spam.values():
    print("True")
if "color" in spam.keys():
    print("True")
else:
    print("False")
if "color" not in spam.keys():
    print("True")
else:
    print("False")


picnicItems = {"apples": 5, "cups": 2}
print("I am bringing " + str(picnicItems.get("cups", 0)) + " cups.")
print("I am bringing " + str(picnicItems.get("eggs", 0)) + " eggs.")
"""

spam = {"name": "Pooka", "age": 5}
spam.setdefault("color", "black")
print(spam)
spam.setdefault("color", "white")
print(spam)
