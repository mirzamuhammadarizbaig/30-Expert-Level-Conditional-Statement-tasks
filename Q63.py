print("-----COOKING RECIPE SUGGESTION-----\n")

ingredient = input("Enter your main ingredient (Chicken/Rice/Potato/Egg):\n").lower()
spiceLevel = input("Preferred spice level (Mild/Medium/Spicy):\n").lower()

if ingredient == "chicken":
    if spiceLevel == "spicy":
        print("Suggested recipe: Spicy Chicken Karahi")
    elif spiceLevel == "medium":
        print("Suggested recipe: Chicken Curry")
    else:
        print("Suggested recipe: Grilled Chicken")

elif ingredient == "rice":
    if spiceLevel == "spicy":
        print("Suggested recipe: Spicy Biryani")
    else:
        print("Suggested recipe: Vegetable Pulao")

elif ingredient == "potato":
    print("Suggested recipe: Aloo Fry")

elif ingredient == "egg":
    time = int(input("How many minutes do you have to cook?\n"))
    if time < 10:
        print("Suggested recipe: Boiled Egg")
    else:
        print("Suggested recipe: Egg Omelette")

else:
    print("No recipe found for this ingredient")
