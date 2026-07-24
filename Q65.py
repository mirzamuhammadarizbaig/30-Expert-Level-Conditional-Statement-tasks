print("-----GAMING TOURNAMENT MATCHMAKING-----\n")

rank = input("Enter your rank (Bronze/Silver/Gold/Platinum):\n").lower()
ping = int(input("Enter your connection ping (ms):\n"))

if ping > 150:
    print("Connection too unstable for ranked matchmaking")
else:
    if rank == "bronze":
        print("Matched with Bronze tier players")
    elif rank == "silver":
        print("Matched with Silver tier players")
    elif rank == "gold":
        if ping < 50:
            print("Matched with Gold/Platinum players (low ping bonus)")
        else:
            print("Matched with Gold tier players")
    elif rank == "platinum":
        print("Matched with Platinum tier players in championship queue")
    else:
        print("Invalid rank entered")
