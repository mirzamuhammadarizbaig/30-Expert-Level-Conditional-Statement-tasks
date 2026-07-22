print("-----DICE GAME-----\n")

diceNumber=4

guess=int(input("Guess the dice number (1-6)\n"))

if guess==diceNumber:
    print("Congratulations! You Win!")

elif guess==diceNumber-1 or guess==diceNumber+1:
    print("Almost! Try Again.")

else:
    print("You Lose!")