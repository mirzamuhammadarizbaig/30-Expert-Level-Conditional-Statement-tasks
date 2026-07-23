print("-----ELECTION VOTING ELIGIBILITY-----\n")

age = int(input("Enter your age:\n"))
citizen = input("Are you a registered citizen? (yes/no):\n").lower()

if citizen == "yes":
    if age >= 18:
        idCard = input("Do you have a valid ID card? (yes/no):\n").lower()
        if idCard == "yes":
            print("You are eligible to vote")
        else:
            print("You need a valid ID card to vote")
    else:
        print("You must be at least 18 years old to vote")
else:
    print("Only registered citizens can vote")
