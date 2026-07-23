print("-----ONLINE SHOPPING DISCOUNT-----\n")

cartTotal = int(input("Enter your cart total:\n"))
member = input("Are you a premium member? (yes/no):\n").lower()

if cartTotal >= 5000:
    if member == "yes":
        discount = 0.30
    else:
        discount = 0.20
elif cartTotal >= 2000:
    if member == "yes":
        discount = 0.15
    else:
        discount = 0.10
else:
    if member == "yes":
        discount = 0.05
    else:
        discount = 0

finalPrice = cartTotal - (cartTotal * discount)
print("Discount applied:", discount * 100, "%")
print("Final price:", finalPrice)
