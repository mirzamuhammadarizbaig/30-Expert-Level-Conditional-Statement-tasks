print("-----ALIEN COMMUNICATION SYSTEM-----\n")


signal=input("Signal detected? (yes/no)\n").lower()
strength=int(input("Enter Signal Strength (0-100)\n"))
threat=input("Threat level (low/medium/high)\n").lower()
language=input("Language understood? (yes/no)\n").lower()


if threat=="high" or strength<20:
    print("Dangerous Signal! Shutdown System")


elif signal=="yes" and strength>=70 and threat=="low" and language=="yes":
    print("Friendly Contact Established")


elif signal=="yes" and strength>=40:
    print("Unknown Signal - Observe Carefully")


else:
    print("No Alien Communication Found")