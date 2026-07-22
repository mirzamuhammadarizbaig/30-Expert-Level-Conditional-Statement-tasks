print("-----FOOTBALL MATCH PREDICTION-----\n")

team1=input("Enter Team 1 name\n")
team2=input("Enter Team 2 name \n")

currentTime=float(input("Enter Current time (minutes)\n"))

team1Goals=int(input(team1 + " goals?\n"))
team2Goals=int(input(team2 + " goals?\n"))

team1Shots=int(input(team1 + " shots?\n"))
team2Shots=int(input(team2 + " shots?\n"))

team1Possession=int(input(team1 + " Possesion %\n"))
team2Possession=int(input(team2 + " Possesion %\n"))

team1Fouls=int(input(team1 + " Fouls\n"))
team2Fouls=int(input(team2 + " Fouls\n"))

team1Red=int(input(team1 + " Red cards?\n"))
team2Red=int(input(team2 + " Red cards?\n"))

attacking=input("Who is attacking? (team1/team2)\n").lower()

team1Score=0
team2Score=0

if team1Goals>team2Goals:
    team1Score+=5

elif team2Goals>team1Goals:
    team2Score+=5

else:
    team1Score+=1
    team2Score+1

if team1Shots>team2Shots:
    team1Score+=2

elif team2Shots>team1Shots:
    team2Score+=2

if team1Possession>team2Possession:
    team1Score+=2

elif team2Possession>team1Possession:
    team2Score+=2

if team1Fouls>team2Fouls:
    team1Score-=1

elif team2Fouls>team1Fouls:
    team2Score-=1

if team1Red>0:
    team1Score-=5

if team2Red>0:
    team2Score-=5

if attacking=="team1":
    team1Score+=2

elif attacking=="team2":
    team2Score+=2

print("\n-----MATCH ANALYSIS-----")

print(team1,"Score:",team1Score)
print(team2,"Score:",team2Score)

if team1Score>team2Score:
    print(team1,"is most likely to win!")

elif team2Score>team1Score:
    print(team2,"is most likely to win!")

else:
    print("Match is likely to be a Draw")


if currentTime>=80:
    print("Late game situation - anything can happen!")

elif currentTime<45:
    print("First half is still remaining")
