print("-----FLIGHT BOOKING SYSTEM-----\n")

destination = input("Enter destination (Domestic/International):\n").lower()
age = int(input("Enter your age:\n"))

if destination == "domestic":
    seatClass = input("Choose class (Economy/Business):\n").lower()
    if seatClass == "economy":
        print("Ticket price: 15000")
    elif seatClass == "business":
        print("Ticket price: 35000")
    else:
        print("Invalid class")

elif destination == "international":
    if age < 18:
        guardian = input("Are you traveling with a guardian? (yes/no):\n").lower()
        if guardian == "yes":
            print("Booking allowed with guardian consent")
        else:
            print("Minors cannot travel internationally alone")
    else:
        passportValid = input("Is your passport valid for 6+ months? (yes/no):\n").lower()
        if passportValid == "yes":
            print("Booking confirmed for international flight")
        else:
            print("Renew your passport before booking")

else:
    print("Invalid destination type")
