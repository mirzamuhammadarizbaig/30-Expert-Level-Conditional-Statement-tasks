print("-----TAXI FARE CALCULATOR-----\n")

distance=float(input("Enter the distance (km)\n"))
time=input("Day OR Night\n").lower()

baseFare=5

if time=="day":
    total=baseFare+(distance*2)

elif time=="night":
    total=baseFare+(distance*3)

else:
    print("Invalid Choice")

if distance>20:
    discount=total*0.10
    total=total-discount
    print("10% Long Distance Discount Applied")

print("Total Fare =", total)