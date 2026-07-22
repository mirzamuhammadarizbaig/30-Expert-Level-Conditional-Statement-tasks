print("-----PASSWORD SECURITY CHECKER-----\n")


length=int(input("Enter Password Length\n"))
number=input("Has Number? (yes/no)\n").lower()
special=input("Has Special Character? (yes/no)\n").lower()
uppercase=input("Has Uppercase Letter? (yes/no)\n").lower()

if length>=8 and number=="yes" and special=="yes" and uppercase=="yes":
    print("Strong Password")


elif length>=6 and (number=="yes" or uppercase=="yes"):
    print("Medium Password")


else:
    print("Weak Password")