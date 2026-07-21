print("Welcome to the mysterious castle\n")
print("\nFind a way to escape")

health=100
gold=0
hasKey=False

door=input(
    "1.Left\n"
    "2.Right\n"
    "3.Straight\n"
).lower()

if door=="left":
    print("You Enter an old library\n")

    choice=input(
        "1.Read the book\n"
        "2.Open the chest\n"
    )

    if choice=="1":
        print("You found a hidden key")
        hasKey=True

        print("You discover Another door\n")

        nextChoice=input(
            "1.Enter a secret room\n"
            "2.Leave"
        )

        if nextChoice=="1":
            print("You found a treasure\n")
            gold+=500
            print("Gold", gold)
            print("Rich Ending")

        else:
            print("You have Safely escaped the castle")

    elif choice=="2":
        if hasKey:
            print("You Opened the chest\n")
            gold+=200
            print("Gold=", gold)
        else:
            print("Chest is locked, you need to find a key")

elif door=="right":
    print("A monster Appears\n")
    action=input(
        "1.Fight\n"
        "2.Run\n"
    )

    if action=="1":
        health -=50
        if health >0:
            print("You defeated the monster")
            print("Health=",health)
            print("You Escaped!")

        else:
            print("You died")

    elif action=="2":
        print("The monster catches you")
        print("Game Over he ate you alive")

elif door=="straight":
    print("A dragon is sleeping\n")

    dragon=input(
        "1.Sneak past by\n"
        "2.Attack\n"
    )

    if dragon=="1":
        print("you succesfully escaped\n")
        print("VICTORY!")

    elif dragon=="2":
        print("The dragon wakes up")
        print("Game Over , You are burned Alive")

else:
    print("Invalid choice")