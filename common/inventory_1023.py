from item_1023 import item

items = []

items.append(item("123", "Socks (white)"))
i = item("ABC", "Shoes (black)")
items.append(i)
items.append(item("XYZ", "Zipper"))

def show_all_items():
    global items

    for i in items:
        i.showStatus()

def adjust_all_inventory(amount):
    global items

    for i in items:
        # i.quantity += amount
        i.add_quantity(amount)

show_all_items()
adjust_all_inventory(3)
show_all_items()
