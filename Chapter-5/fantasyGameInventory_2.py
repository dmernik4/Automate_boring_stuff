def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    # the code
    for loot in dragonLoot:
        if loot not in inv:
            inv[loot] = 1
        else:
            inv[loot] += 1


inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

addToInventory(inv, dragonLoot)

displayInventory(inv)
