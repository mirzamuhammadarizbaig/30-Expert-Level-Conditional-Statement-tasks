print("\n-----CAR RENTAL-----")

print(
    "Toyota corolla\n"
    "BMW M5\n"
    "Buggatti chiron\n"
)

car=input("Enter the car name you want to rent")

age=int(input("Enter your age\n"))
license=input("Do you have driving license?\n")

if age>18:
    print("You are too young to rent a car")

elif license=="no":
    print("Driving license required")

else:
    ("Car rental Approved for",car)

