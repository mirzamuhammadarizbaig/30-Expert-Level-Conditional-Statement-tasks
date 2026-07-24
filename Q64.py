print("-----BLOOD DONATION ELIGIBILITY-----\n")

age = int(input("Enter your age:\n"))
weight = int(input("Enter your weight in kg:\n"))
lastDonation = int(input("Enter days since last donation (0 if never):\n"))

if age < 18 or age > 65:
    print("Not eligible: Age must be between 18 and 65")
else:
    if weight < 50:
        print("Not eligible: Minimum weight requirement is 50kg")
    else:
        if lastDonation == 0:
            print("Eligible to donate blood")
        elif lastDonation >= 90:
            print("Eligible to donate blood")
        else:
            daysLeft = 90 - lastDonation
            print("Not eligible yet, wait", daysLeft, "more days")
