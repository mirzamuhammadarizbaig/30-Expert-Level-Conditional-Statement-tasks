print("-----SMART FRIDGE INVENTORY-----\n")

milkLevel = int(input("Enter milk level percentage:\n"))
eggsCount = int(input("Enter number of eggs left:\n"))

if milkLevel < 20:
    print("Alert: Milk running low, add to shopping list")
else:
    print("Milk level sufficient")

if eggsCount < 3:
    if eggsCount == 0:
        print("Alert: No eggs left, add to shopping list")
    else:
        print("Alert: Eggs running low, add to shopping list")
else:
    print("Egg supply sufficient")

expiryDays = int(input("Enter days until nearest item expires:\n"))
if expiryDays <= 1:
    print("Urgent: An item expires soon, use it today")
elif expiryDays <= 3:
    print("Reminder: An item will expire soon")
