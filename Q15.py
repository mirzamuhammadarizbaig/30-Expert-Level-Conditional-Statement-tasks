print("-----MAGIC SPELL CHOOSER-----\n")

spell=input("Choose a spell (Fire/Ice/Lightning)\n").lower()

if spell=="fire":
    print("You burned the enemy!")

elif spell=="ice":
    print("You froze the enemy!")

elif spell=="lightning":
    print("You shocked the enemy!")

else:
    print("Unknown Spell!")