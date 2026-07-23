print("-----FITNESS TRACKER-----\n")

steps = int(input("Enter number of steps walked today:\n"))
duration = int(input("Enter workout duration in minutes:\n"))

if steps >= 10000:
    print("Goal achieved! Great job")
    caloriesBurned = steps * 0.04
elif steps >= 5000:
    print("Halfway there, keep going")
    caloriesBurned = steps * 0.035
else:
    print("You need to walk more today")
    caloriesBurned = steps * 0.03

if duration > 60:
    caloriesBurned += 100
    print("Bonus calories added for long workout")

print("Estimated calories burned:", caloriesBurned)
