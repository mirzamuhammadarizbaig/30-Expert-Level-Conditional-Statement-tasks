print("-----SUPERHERO POWER SELECTOR-----\n")

power = input("Choose your power (Strength/Speed/Flight/Invisibility):\n").lower()

if power == "strength":
    level = int(input("Enter strength level (1-10):\n"))
    if level >= 8:
        print("You can lift a truck!")
    elif level >= 5:
        print("You can lift a car!")
    else:
        print("You can lift heavy furniture")

elif power == "speed":
    level = int(input("Enter speed level (1-10):\n"))
    if level >= 8:
        print("You can outrun a car!")
    else:
        print("You are faster than an average human")

elif power == "flight":
    altitude = int(input("Enter max altitude in meters:\n"))
    if altitude > 1000:
        print("You can fly above the clouds!")
    else:
        print("You can fly over buildings")

elif power == "invisibility":
    duration = int(input("Enter duration in minutes:\n"))
    if duration > 30:
        print("You can vanish for a long mission!")
    else:
        print("You can vanish for a quick escape")

else:
    print("Unknown power, defaulting to normal human")
