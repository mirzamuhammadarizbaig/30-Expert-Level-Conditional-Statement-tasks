print("-----NINJA TRAINING DOJO-----\n")

rank = input("Enter your current ninja rank (Genin/Chunin/Jonin):\n").lower()

if rank == "genin":
    stealthScore = int(input("Enter your stealth test score:\n"))
    if stealthScore >= 80:
        print("Promoted to Chunin rank!")
    else:
        print("Keep training, try again next season")

elif rank == "chunin":
    missionsCompleted = int(input("Enter number of missions completed:\n"))
    if missionsCompleted >= 10:
        combatScore = int(input("Enter your combat exam score:\n"))
        if combatScore >= 85:
            print("Promoted to Jonin rank!")
        else:
            print("Failed combat exam, remain Chunin")
    else:
        print("Complete more missions before promotion exam")

elif rank == "jonin":
    print("You are already at the highest rank, consider becoming a sensei")

else:
    print("Invalid rank entered")
