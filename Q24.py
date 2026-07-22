print("-----DNA COMPATIBILITY SCANNER-----\n")

age1=int(input("Enter First Person Age\n"))
age2=int(input("Enter Second Person Age\n"))

health=input("Health Status (good/bad)\n").lower()

score=int(input("Enter Compatibility Score (0-100)\n"))

ageDifference=abs(age1-age2)


if score>=90 and health=="good" and ageDifference<=10:
    print("Perfect Match")


elif score>=70 and health=="good":
    print("Possible Match")


else:
    print("Not Compatible")