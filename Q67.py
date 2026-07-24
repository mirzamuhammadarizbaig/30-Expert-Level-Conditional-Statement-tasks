print("-----TAX CALCULATOR SYSTEM-----\n")

income = int(input("Enter your annual income:\n"))
isFiler = input("Are you a registered tax filer? (yes/no):\n").lower()

if income <= 600000:
    tax = 0
elif income <= 1200000:
    tax = (income - 600000) * 0.05
elif income <= 2400000:
    tax = 30000 + (income - 1200000) * 0.10
else:
    tax = 150000 + (income - 2400000) * 0.15

if isFiler == "no":
    tax = tax * 1.5
    print("Non-filer surcharge applied")

print("Total tax payable:", tax)
