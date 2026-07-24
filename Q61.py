print("-----TREASURE MAP DECODER-----\n")

symbol = input("Enter the symbol found on the map (Skull/Star/Anchor/Compass):\n").lower()

if symbol == "skull":
    print("Danger ahead! Proceed with caution")
    hasWeapon = input("Do you have a weapon? (yes/no):\n").lower()
    if hasWeapon == "yes":
        print("You fight off the guardians and continue")
    else:
        print("You retreat to find better equipment")

elif symbol == "star":
    print("You found a clue leading closer to the treasure!")

elif symbol == "anchor":
    print("The treasure is near the coast")
    tideLevel = input("Is the tide low? (yes/no):\n").lower()
    if tideLevel == "yes":
        print("You can reach the hidden cave now!")
    else:
        print("Wait for low tide to access the cave")

elif symbol == "compass":
    print("Follow the compass north to continue your journey")

else:
    print("Unknown symbol, the map is unreadable here")
