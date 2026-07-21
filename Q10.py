print("\n-----HOSPITAL OF MITI-----")

age=int(input("Enter your age\n"))
print("Emergency?\n")
emergency=input("High Or Medium Or Low\n").lower()

if emergency=="high":
    print("Immediate treatment required\n")

elif emergency=="medium":
    print("Please wait for your turn\n")

elif emergency=="low":
    print("Visit the general doctor\n")

else:
    print("invalid choice!\n")

if age>=60:
    print("Senior Citizen priority")