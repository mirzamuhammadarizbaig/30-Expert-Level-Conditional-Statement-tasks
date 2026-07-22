print("-----PIRATE TREASURE HUNT-----\n")

chest=int(input(
    "Choose a Treasure Chest\n"
    "1.Chest 1\n"
    "2.Chest 2\n"
    "3.Chest 3\n"
))

if chest==1:
    print("You found 100 Gold Coins!")

elif chest==2:
    print("A Snake Bit You!")
    print("Game Over")

elif chest==3:
    print("Congratulations!")
    print("You found a Diamond!")

else:
    print("Invalid Chest")