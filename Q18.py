print("-----ROBOT ASSISTANT-----\n")

battery=int(input("Enter Battery Percentage\n"))
command=input("Clean OR Cook OR Dance\n").lower()

if battery<20:
    print("Low Battery!")
    print("Please Charge Me")

elif command=="clean":
    print("Cleaning the House...")

elif command=="cook":
    print("Preparing Your Meal...")

elif command=="dance":
    print("Dancing...")

else:
    print("Unknown Command")