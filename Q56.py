print("-----CAR PARKING SYSTEM-----\n")

slotsAvailable = int(input("Enter number of available parking slots:\n"))

if slotsAvailable == 0:
    print("Parking full, please wait")
else:
    vehicleType = input("Enter vehicle type (Car/Bike/Truck):\n").lower()

    if vehicleType == "car":
        fee = 100
    elif vehicleType == "bike":
        fee = 50
    elif vehicleType == "truck":
        if slotsAvailable >= 2:
            fee = 200
        else:
            print("Not enough space for truck parking")
            fee = 0
    else:
        print("Unknown vehicle type")
        fee = 0

    if fee > 0:
        print("Parking fee:", fee)
        print("Slots remaining:", slotsAvailable - 1)
