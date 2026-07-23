print("-----ZOO ANIMAL FEEDING SYSTEM-----\n")

animal = input("Enter animal name (Lion/Elephant/Monkey/Penguin):\n").lower()

if animal == "lion":
    time = input("Is it feeding time? (yes/no):\n").lower()
    if time == "yes":
        print("Feed the lion 5kg of meat")
    else:
        print("Not feeding time, do not disturb the lion")

elif animal == "elephant":
    weight = int(input("Enter elephant weight in kg:\n"))
    if weight > 4000:
        print("Feed 150kg of plants")
    else:
        print("Feed 100kg of plants")

elif animal == "monkey":
    print("Feed bananas and fruits")

elif animal == "penguin":
    temperature = int(input("Enter enclosure temperature:\n"))
    if temperature < 10:
        print("Feed fish, healthy environment")
    else:
        print("Warning: enclosure too warm for penguins!")

else:
    print("Unknown animal, consult the zookeeper")
