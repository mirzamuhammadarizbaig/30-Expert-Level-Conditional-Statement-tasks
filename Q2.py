purchaseAmount=float(input("Enter the purchase amount:\n"))
memberShip=input("Yes OR No\n")
coupon=input("Enter your coupn code press 'N' if you dont have any\n") 

total=purchaseAmount
print("Total",total)

if memberShip=="yes":
   total=total * 0.85
   print("15% member Discount Applied")

if coupon=="SAVE10":
   total=total * 0.90
   print("10% couponDiscount Applied")

if total<100:
   Shipping=0
   print("Free Shipping!")

else:
   Shipping=8
   print("Shipping fees = 8$")

finalBill=total+Shipping

print("HERE IS YOUR BILL")
print("Total Amount of purchase: $",purchaseAmount)
print("Total After Discount: $", total)
print("Shipping fee =",Shipping)
print("Final Amount", finalBill)

