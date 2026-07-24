print("-----VIDEO GAME LEVEL UP SYSTEM-----\n")

xp = int(input("Enter your current XP:\n"))
level = int(input("Enter your current level:\n"))

if xp >= 1000:
    level += 1
    print("Level up! You are now level", level)

    bonus = input("Choose a bonus (Health/Attack/Defense):\n").lower()
    if bonus == "health":
        print("Health increased by 50")
    elif bonus == "attack":
        print("Attack increased by 20")
    elif bonus == "defense":
        print("Defense increased by 15")
    else:
        print("Invalid bonus choice, no stat increased")

elif xp >= 500:
    print("Halfway to next level, keep grinding")
else:
    print("Keep playing to earn more XP")

if level >= 10:
    print("You have unlocked a new skill tree!")
