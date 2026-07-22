print("-----FORMULA RACING STRATEGY-----\n")


tire=input("Tire condition (good/bad)\n").lower()
fuel=int(input("Enter Fuel Percentage\n"))
weather=input("Weather (dry/rain)\n").lower()
damage=int(input("Enter Car Damage Percentage\n"))


if tire=="good" and fuel>=70 and weather=="dry" and damage<20:
    print("Attack Mode! Push Maximum Speed")


elif tire=="bad" or fuel<30:
    print("Pit Stop Required")


elif damage<50 and fuel>=30:
    print("Continue Racing Carefully")


else:
    print("Car Too Damaged! Retire From Race")