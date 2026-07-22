print("-----SPACE MISSION LAUNCH-----\n")

fuel=int(input("Enter Fuel Level (%)\n"))
weather=input("Good OR Bad\n").lower()

if fuel>=80 and weather=="good":
    print("Mission Launched Successfully!")

elif fuel<80:
    print("Mission Delayed!")
    print("Not Enough Fuel")

elif weather=="bad":
    print("Mission Delayed!")
    print("Bad Weather")

else:
    print("Launch Cancelled")