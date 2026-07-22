print("-----PHONE BATTERY SAVER-----\n")

battery=int(input("Enter Battery Percentage\n"))
charger=input("Is Charger Connected? (yes/no)\n").lower()

if battery<=20 and charger=="no":
    print("Battery Saver Mode Enabled")

elif charger=="yes":
    print("Phone Charging...")

elif battery>80:
    print("Battery Fully Charged")

else:
    print("Battery Level Normal")