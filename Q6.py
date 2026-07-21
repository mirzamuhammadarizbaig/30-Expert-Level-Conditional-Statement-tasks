print("\n-----AIRPORT SECURITY CHECKER-----")

passport=input("Do you have your passport\n")
ticket=input("Do you have your ticket?\n")
items=input("Are you carrying some porihibbated items\n")

if passport=="no":
    print("Entry Denied")

elif ticket=="no":
    print("Ticket Required")

elif items=="yes":
    print("Security Alert")

else:
    print("Welcome!, You may board the plane")
