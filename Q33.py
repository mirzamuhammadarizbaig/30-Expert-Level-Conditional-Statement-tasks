print("-----RESTAURANT ORDER SYSTEM-----\n")

order = input("What would you like to order (Pizza/Burger/Salad):\n").lower()

if order == "pizza":
    size = input("Choose size (Small/Medium/Large):\n").lower()
    if size == "small":
        price = 500
    elif size == "medium":
        price = 800
    elif size == "large":
        price = 1200
    else:
        price = 0
        print("Invalid size")

    if price > 0:
        extra = input("Add extra cheese? (yes/no):\n").lower()
        if extra == "yes":
            price += 100
        print("Total price:", price)

elif order == "burger":
    combo = input("Do you want a combo meal? (yes/no):\n").lower()
    if combo == "yes":
        print("Total price: 650")
    else:
        print("Total price: 400")

elif order == "salad":
    print("Total price: 300")

else:
    print("Item not available")
