print("\n-----WELCOME TO TEKKEN-----")

player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")

player1Health = 100
player2Health = 100

print("\nGAME STARTS NOW!\n")

moveP1 = int(input(
f"{player1}, choose your move\n"
"1. Punch\n"
"2. Kick\n"
"3. Block\n"
"4. Special Attack\n"
))

moveP2 = int(input(
f"{player2}, choose your move\n"
"1. Punch\n"
"2. Kick\n"
"3. Block\n"
"4. Special Attack\n"
))

if moveP1 == 1 and moveP2 == 1:
    player1Health -= 10
    player2Health -= 10
    print("Both players punched!")

elif moveP1 == 1 and moveP2 == 2:
    player1Health -= 15
    player2Health -= 10
    print(f"{player2} wins the exchange with a Kick!")

elif moveP1 == 2 and moveP2 == 1:
    player1Health -= 10
    player2Health -= 15
    print(f"{player1} wins the exchange with a Kick!")

elif moveP1 == 2 and moveP2 == 2:
    player1Health -= 15
    player2Health -= 15
    print("Both players kicked!")

elif moveP1 == 1 and moveP2 == 3:
    player2Health -= 5
    print(f"{player2} blocked the punch!")

elif moveP1 == 3 and moveP2 == 1:
    player1Health -= 5
    print(f"{player1} blocked the punch!")

elif moveP1 == 2 and moveP2 == 3:
    player2Health -= 7
    print(f"{player2} blocked the kick!")

elif moveP1 == 3 and moveP2 == 2:
    player1Health -= 7
    print(f"{player1} blocked the kick!")

elif moveP1 == 3 and moveP2 == 3:
    print("Both players blocked. No damage!")

elif moveP1 == 4 and moveP2 == 1:
    if player1Health <= 50:
        player2Health -= 30
        player1Health -= 10
        print(f"{player1} landed a Special Attack!")
    else:
        print("Special Attack Locked!")

elif moveP1 == 1 and moveP2 == 4:
    if player2Health <= 50:
        player1Health -= 30
        player2Health -= 10
        print(f"{player2} landed a Special Attack!")
    else:
        print("Special Attack Locked!")

else:
    print("This move combination isn't implemented yet.")

print("\nRESULT")
print(f"{player1}: {player1Health} HP")
print(f"{player2}: {player2Health} HP")

if player1Health > player2Health:
    print(f"{player1} Wins!")
elif player2Health > player1Health:
    print(f"{player2} Wins!")
else:
    print("Draw!")