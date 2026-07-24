print("-----WEATHER SATELLITE ALERT-----\n")

windSpeed = int(input("Enter wind speed (km/h):\n"))
pressureDrop = int(input("Enter pressure drop rate (hPa/hr):\n"))

if windSpeed >= 120:
    print("SEVERE ALERT: Cyclone conditions detected!")
    coastalArea = input("Is this a coastal area? (yes/no):\n").lower()
    if coastalArea == "yes":
        print("Issue immediate evacuation order")
    else:
        print("Issue high wind warning")

elif windSpeed >= 60 or pressureDrop >= 10:
    print("Storm warning issued, monitor conditions closely")

else:
    print("Weather conditions stable")
