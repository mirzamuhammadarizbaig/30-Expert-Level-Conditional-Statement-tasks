print("-----HUMAN BRAIN TEST-----\n")


sleep=int(input("How many hours do you sleep?\n"))
stress=input("Stress level (low/medium/high)\n").lower()
exercise=int(input("Exercise days per week\n"))


if sleep>=7 and stress=="low" and exercise>=3:
    print("Healthy Brain")


elif sleep>=6 and exercise>=1:
    print("Improve Your Lifestyle")


else:
    print("Warning: Unhealthy Routine")