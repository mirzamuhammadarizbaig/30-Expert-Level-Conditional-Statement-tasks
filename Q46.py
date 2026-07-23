print("-----LIBRARY BOOK FINE CALCULATOR-----\n")

daysLate = int(input("Enter number of days the book is late:\n"))
memberType = input("Enter membership type (Student/Regular/Premium):\n").lower()

if daysLate <= 0:
    print("No fine, book returned on time")
else:
    if memberType == "student":
        finePerDay = 5
    elif memberType == "regular":
        finePerDay = 10
    elif memberType == "premium":
        finePerDay = 3
    else:
        finePerDay = 10
        print("Unknown membership, applying regular rate")

    totalFine = daysLate * finePerDay

    if totalFine > 200:
        print("Fine capped at maximum limit: 200")
    else:
        print("Total fine:", totalFine)
