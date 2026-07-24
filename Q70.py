print("-----CONCERT TICKET PRICING-----\n")

seatZone = input("Choose seat zone (Front/Middle/Back):\n").lower()
isEarlyBird = input("Are you buying during early bird sale? (yes/no):\n").lower()

if seatZone == "front":
    price = 8000
elif seatZone == "middle":
    price = 5000
elif seatZone == "back":
    price = 2500
else:
    price = 0
    print("Invalid seat zone")

if price > 0:
    if isEarlyBird == "yes":
        price = price * 0.8
        print("Early bird discount applied!")

    print("Final ticket price:", price)
