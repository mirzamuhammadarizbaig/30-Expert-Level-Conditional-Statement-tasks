print("-----TRAFFIC LIGHT SIMULATOR-----\n")

light = input("Enter current light color (Red/Yellow/Green):\n").lower()
pedestrian = input("Is a pedestrian waiting? (yes/no):\n").lower()

if light == "red":
    print("STOP the vehicle")
    if pedestrian == "yes":
        print("Pedestrians may cross now")

elif light == "yellow":
    speed = int(input("Enter your current speed (km/h):\n"))
    if speed > 40:
        print("Proceed with caution, too late to stop safely")
    else:
        print("Slow down and prepare to stop")

elif light == "green":
    print("GO")
    if pedestrian == "yes":
        print("Warning: pedestrian waiting, drive carefully")

else:
    print("Invalid light color")
