print("-----MARS MISSION CONTROLLER-----\n")


fuel=int(input("Enter Fuel Percentage\n"))
oxygen=int(input("Enter Oxygen Percentage\n"))
engine=input("Engine Status (working/fault)\n").lower()
weather=input("Weather (good/bad)\n").lower()


if fuel>=80 and oxygen>=70 and engine=="working" and weather=="good":
    print("Mission Launched Successfully!")


elif engine=="fault" or oxygen<70:
    print("Mission Aborted")


elif fuel<80 or weather=="bad":
    print("Mission Delayed")


else:
    print("Mission Cancelled")