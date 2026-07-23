print("-----WIZARD DUEL-----\n")

myHealth = 100
enemyHealth = 100

spell = input("Cast a spell (Fireball/IceShard/Lightning/Heal):\n").lower()

if spell == "fireball":
    damage = 30
    enemyHealth -= damage
    print("Fireball hits! Enemy health:", enemyHealth)

elif spell == "iceshard":
    damage = 20
    enemyHealth -= damage
    freeze = input("Enemy is frozen, attack again? (yes/no):\n").lower()
    if freeze == "yes":
        enemyHealth -= 15
    print("Enemy health:", enemyHealth)

elif spell == "lightning":
    damage = 40
    mana = int(input("Enter your remaining mana:\n"))
    if mana >= 20:
        enemyHealth -= damage
        print("Lightning strikes hard! Enemy health:", enemyHealth)
    else:
        print("Not enough mana to cast this spell!")

elif spell == "heal":
    myHealth += 25
    if myHealth > 100:
        myHealth = 100
    print("You healed! Your health:", myHealth)

else:
    print("Invalid spell, you wasted your turn!")

if enemyHealth <= 0:
    print("You defeated the enemy wizard!")
