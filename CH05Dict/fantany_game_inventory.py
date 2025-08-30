# inventory.py
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#
# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + ' ' + k)
#         item_total += v
#     print("Total number of items: " + str(item_total))
#
# displayInventory(stuff)

### Re worked the script above
stuff = {'rope' : 1, 'torch' : 6, 'gold coin' : 12, 'dagger' : 1, 'arrow' : 7 }

def displayInventory(inventory):
    print('Inventory:')
    total_inventory = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_inventory += v
    print('Total number of items is: ' + str(total_inventory))

displayInventory(stuff)