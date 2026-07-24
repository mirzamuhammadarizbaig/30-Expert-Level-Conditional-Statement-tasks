print("-----DRAGON RIDER TRAINING-----\n")

bondLevel = int(input("Enter your bond level with the dragon (0-100):\n"))

if bondLevel < 30:
    print("Your dragon does not trust you yet, keep training together")
else:
    dragonType = input("Choose dragon type (Fire/Ice/Storm):\n").lower()

    if dragonType == "fire":
        if bondLevel >= 70:
            print("You can now perform the Inferno Dive maneuver!")
        else:
            print("You can fly short distances with your fire dragon")

    elif dragonType == "ice":
        if bondLevel >= 70:
            print("You can now perform the Frost Breath attack!")
        else:
            print("You can glide with your ice dragon")

    elif dragonType == "storm":
        if bondLevel >= 90:
            print("You can summon lightning storms!")
        else:
            print("Your storm dragon needs a stronger bond for storm powers")

    else:
        print("Unknown dragon type")
