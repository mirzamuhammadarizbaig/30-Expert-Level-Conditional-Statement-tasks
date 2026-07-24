print("-----WATER TANK LEVEL CONTROLLER-----\n")

waterLevel = int(input("Enter current water level percentage:\n"))
motorStatus = input("Is the motor currently ON? (yes/no):\n").lower()

if waterLevel <= 20:
    if motorStatus == "no":
        print("Motor turned ON to fill the tank")
    else:
        print("Motor already running, filling in progress")

elif waterLevel >= 95:
    if motorStatus == "yes":
        print("Tank full, motor turned OFF")
    else:
        print("Tank is full, no action needed")

else:
    print("Water level is normal, no action taken")
