print("-----WEREWOLF TRANSFORMATION SYSTEM-----\n")

moonPhase = input("Enter current moon phase (Full/Half/New):\n").lower()

if moonPhase == "full":
    controlLevel = int(input("Enter your self control level (0-100):\n"))
    print("You are transforming into a werewolf!")

    if controlLevel >= 70:
        print("You maintain control over your instincts")
    elif controlLevel >= 40:
        print("You feel the urge to hunt, stay cautious")
    else:
        print("Danger: You have lost control!")

elif moonPhase == "half":
    print("Partial transformation: heightened senses only")

elif moonPhase == "new":
    print("No transformation, you remain human tonight")

else:
    print("Invalid moon phase")
