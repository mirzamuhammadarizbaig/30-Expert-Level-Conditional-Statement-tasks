print("-----WEDDING PLANNER BUDGET-----\n")

totalBudget = int(input("Enter your total wedding budget:\n"))
guestCount = int(input("Enter expected number of guests:\n"))

costPerGuest = 3000
estimatedCost = guestCount * costPerGuest

if estimatedCost > totalBudget:
    print("Budget exceeded! Consider reducing guest count")
    reduceGuests = (estimatedCost - totalBudget) // costPerGuest
    print("Reduce guests by at least:", reduceGuests)
else:
    remaining = totalBudget - estimatedCost
    print("Budget is sufficient, remaining funds:", remaining)

    if remaining >= 500000:
        print("You can afford a luxury venue!")
    elif remaining >= 200000:
        print("You can afford a mid-range venue")
    else:
        print("Consider a budget-friendly venue")
