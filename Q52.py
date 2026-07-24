print("-----PIZZA DELIVERY TRACKER-----\n")

distance = int(input("Enter delivery distance in km:\n"))
weather = input("Enter current weather (Clear/Rainy/Stormy):\n").lower()

if weather == "stormy":
    print("Delivery postponed due to storm")
else:
    if distance <= 5:
        eta = 20
    elif distance <= 10:
        eta = 35
    else:
        eta = 50

    if weather == "rainy":
        eta += 15
        print("Rain detected, delivery may be delayed")

    print("Estimated delivery time:", eta, "minutes")

    if eta > 45:
        print("Free dessert included for the long wait!")
