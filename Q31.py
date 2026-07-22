print("\n-----PET SIMULATOR-----")

name=input("Enter your pet name\n")


happiness=50
hunger=50
energy=50
coins=50

action=int(input(
    "Choose your action\n"
    f"1.Feed {name}\n"
    f"2.Play with {name}\n"
    f"3.Let {name} sleep\n"
    f"4.Check {name} Status\n"
))

if action==1:
    hunger-=20
    happiness+=10
    coins-=10
    print(f"{name} is eating")

    choose=int(input(
        f"1.Feed {name} again\n"
        f"2.Let {name} sleep\n"
        f"3.Check {name} status\n"
    ))

    if choose==1:
       
        hunger-=30
        happiness+=5
        coins-=15
        print(f"{name} is eating")
        print(f"{name} is not hungry anymore")

        chooseAgain=int(input(f"1.Check {name} status\n"))

        if chooseAgain==1:
           print(f"Here is {name} Status")
           print("Happiness=",happiness)
           print("Hunger=",hunger)
           print("Energy=",energy)
           print("Coins=",coins)

        else:
            print("Invalid Choice")

    elif choose==2:
        energy+=50
        happiness+=10
        hunger-=10
        print(f"{name} is sleeping")

        chooseAgain1=int(input(
            f"1.Check {name} Status\n"
        ))

        if chooseAgain1==1:
            print(f"Here is {name} Status")
            print("Happiness=",happiness)
            print("Hunger=",hunger)
            print("Energy=",energy)
            print("Coins=",coins)

        else:
            print("Invalid Choice")

    elif choose==3:
        print(f"Here is {name} Status")
        print("Happiness=",happiness)
        print("Hunger=",hunger)
        print("Energy=",energy)
        print("Coins=",coins)

    else:
        print("Invalid Choice")

elif action==2:
    energy-=20
    happiness+=50
    hunger-=10
    print(f"{name} is playing")
    print(f"{name} is happy!")

    choiceAgain=int(input(
        f"1.Check {name} Status\n"
    ))

    if choiceAgain==1:
       print(f"Here is {name} Status")
       print("Happiness=",happiness)
       print("Hunger=",hunger)
       print("Energy=",energy)
       print("Coins=",coins)

    else:
        print("Invalid Choice")

if action==3:
    energy+=50
    happiness+=10
    hunger-=10
    print(f"{name} is sleeping")

    chooseAgain2=int(input(
        f"1.Check {name} Status\n"
    ))

    if chooseAgain2==1:
       print(f"Here is {name} Status")
       print("Happiness=",happiness)
       print("Hunger=",hunger)
       print("Energy=",energy)
       print("Coins=",coins)

    else:
        print("Invalid Choice")

if action==4:
    print(f"Here is {name} Status")
    print("Happiness=",happiness)
    print("Hunger=",hunger)
    print("Energy=",energy)
    print("Coins=",coins)


