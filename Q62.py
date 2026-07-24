print("-----ALIEN INVASION DEFENSE-----\n")

shieldEnergy = int(input("Enter shield energy level (0-100):\n"))
enemyCount = int(input("Enter number of enemy ships detected:\n"))

if enemyCount == 0:
    print("No threats detected, stand down")
else:
    if shieldEnergy < 20:
        print("Critical: Shield energy too low, retreat immediately")
    else:
        if enemyCount > 10:
            if shieldEnergy >= 70:
                print("Engage full defense, launching counterattack")
            else:
                print("Too many enemies, activate emergency shield boost")
        elif enemyCount > 3:
            print("Engage standard defense protocol")
        else:
            print("Minor threat, single turret defense sufficient")
