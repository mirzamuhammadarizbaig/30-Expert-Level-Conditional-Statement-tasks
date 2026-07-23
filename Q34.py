print("-----WEATHER ADVISORY SYSTEM-----\n")

temperature = int(input("Enter current temperature (C):\n"))
rain = input("Is it raining? (yes/no):\n").lower()

if temperature > 40:
    print("Heatwave warning! Stay hydrated.")
elif temperature >= 25:
    if rain == "yes":
        print("Warm and rainy, carry an umbrella")
    else:
        print("Pleasant weather")
elif temperature >= 10:
    if rain == "yes":
        print("Cold and rainy, wear a jacket and carry an umbrella")
    else:
        print("Cool weather, a light jacket is enough")
else:
    print("Freezing cold! Wear heavy winter clothes")
