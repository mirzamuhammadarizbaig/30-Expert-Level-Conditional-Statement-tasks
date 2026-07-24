print("-----SUBMARINE DEPTH CONTROL-----\n")

currentDepth = int(input("Enter current depth in meters:\n"))
hullPressureLimit = 500

if currentDepth >= hullPressureLimit:
    print("CRITICAL: Hull pressure limit reached, emergency ascend!")
else:
    action = input("Choose action (Dive/Ascend/Hold):\n").lower()

    if action == "dive":
        diveAmount = int(input("Enter dive depth in meters:\n"))
        newDepth = currentDepth + diveAmount
        if newDepth >= hullPressureLimit:
            print("Warning: This dive would exceed safe depth, aborting")
        else:
            print("Diving to", newDepth, "meters")

    elif action == "ascend":
        print("Ascending to surface")

    elif action == "hold":
        print("Holding current depth at", currentDepth, "meters")

    else:
        print("Invalid command")
