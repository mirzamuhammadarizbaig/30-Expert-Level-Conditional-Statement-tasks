print("-----WAREHOUSE INVENTORY MANAGEMENT-----\n")

stockLevel = int(input("Enter current stock level:\n"))
reorderPoint = int(input("Enter reorder point threshold:\n"))

if stockLevel <= 0:
    print("OUT OF STOCK: Immediate reorder required")
elif stockLevel <= reorderPoint:
    supplierAvailable = input("Is the supplier available today? (yes/no):\n").lower()
    if supplierAvailable == "yes":
        print("Placing reorder now")
    else:
        print("Warning: Stock low, but supplier unavailable")
else:
    demandForecast = input("Is high demand expected this week? (yes/no):\n").lower()
    if demandForecast == "yes":
        print("Stock sufficient for now, but monitor closely")
    else:
        print("Stock level healthy, no action needed")
