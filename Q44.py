print("-----SMART HOME THERMOSTAT-----\n")

currentTemp = int(input("Enter current room temperature:\n"))
mode = input("Enter mode (Auto/Manual):\n").lower()

if mode == "auto":
    if currentTemp > 28:
        print("AC turned ON, cooling to 24 degrees")
    elif currentTemp < 16:
        print("Heater turned ON, warming to 20 degrees")
    else:
        print("Temperature is comfortable, no action needed")

elif mode == "manual":
    targetTemp = int(input("Enter your desired temperature:\n"))
    if targetTemp > currentTemp:
        print("Heater turned ON until target reached")
    elif targetTemp < currentTemp:
        print("AC turned ON until target reached")
    else:
        print("Room is already at desired temperature")

else:
    print("Invalid mode selected")
