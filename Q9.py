print("\n-----HOTEL ROOM BOOKING-----")

nights=int(input("How many night do you want to stay\n"))
print("What Type of room you want")
room=input("Standard or Premium\n").lower()

if room=="standard":
    total=nights*50

elif room=="premium":
    total=nights*100

else:
    print("Invalid room")

if nights>5:
    discount=total*0.10
    total=total-discount
    print("10% Discount Applied")

print("Total Bill is $",total)