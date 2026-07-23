print("-----ZOMBIE SURVIVAL GAME-----\n")

health = 100
ammo = 10

action = input("Zombies are approaching! Fight or Run? (fight/run):\n").lower()

if action == "fight":
    if ammo > 5:
        print("You fought them off easily!")
        health -= 10
    elif ammo > 0:
        print("Tough fight but you survived!")
        health -= 30
    else:
        print("No ammo left! You got bitten!")
        health -= 60

    if health <= 0:
        print("Game Over")
    else:
        print("Remaining health:", health)

elif action == "run":
    stamina = int(input("Enter your stamina (0-100):\n"))
    if stamina > 50:
        print("You escaped safely!")
    elif stamina > 20:
        print("You escaped but got scratched")
        health -= 15
        print("Remaining health:", health)
    else:
        print("You collapsed while running, zombies caught you!")
        health = 0
        print("Game Over")

else:
    print("Invalid action, zombies got you!")
