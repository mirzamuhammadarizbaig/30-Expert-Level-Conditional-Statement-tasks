print("-----FIRE ALARM SYSTEM-----\n")

smokeLevel = int(input("Enter smoke level detected (0-100):\n"))
temperature = int(input("Enter room temperature (C):\n"))

if smokeLevel > 70 or temperature > 60:
    print("FIRE ALARM TRIGGERED!")
    sprinklers = input("Activate sprinklers? (yes/no):\n").lower()
    if sprinklers == "yes":
        print("Sprinklers activated, fire department notified")
    else:
        print("Warning: Sprinklers not activated, evacuate immediately")

elif smokeLevel > 30 or temperature > 40:
    print("Caution: Elevated smoke/temperature levels detected")
else:
    print("All systems normal")
