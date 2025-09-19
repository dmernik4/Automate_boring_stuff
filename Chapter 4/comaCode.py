spam = ["apples", "bannanas", "tofu", "cats", "dogs"]


def printList(list):
    for i in list:
        if i != list[-1]:
            print((i), end=", ")
        else:
            print("and " + (i))


printList(spam)
