# Program that shows the inventory of your Fantasy Game Character

stuff = {"rope": 1, "torch": 6, "golden coin": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


displayInventory(stuff)
