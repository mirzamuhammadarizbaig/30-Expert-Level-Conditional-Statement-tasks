print("-----WI-FI TROUBLESHOOTER-----\n")

wifi=input("Is Wi-Fi turned on? (yes/no)\n").lower()
router=input("Is Router working? (yes/no)\n").lower()
airplane=input("Is Airplane Mode on? (yes/no)\n").lower()

if airplane=="yes":
    print("Turn off Airplane Mode")

elif wifi=="no":
    print("Turn on Wi-Fi")

elif router=="no":
    print("Restart your Router")

else:
    print("Internet Connection Working!")