print("-----BANK LOAN APPROVAL-----\n")

income = int(input("Enter your monthly income:\n"))
creditScore = int(input("Enter your credit score:\n"))
loanAmount = int(input("Enter requested loan amount:\n"))

if creditScore < 500:
    print("Loan rejected: Poor credit score")
else:
    if income >= 100000:
        maxLoan = income * 20
    elif income >= 50000:
        maxLoan = income * 15
    else:
        maxLoan = income * 10

    if loanAmount <= maxLoan:
        if creditScore >= 750:
            print("Loan approved with low interest rate")
        else:
            print("Loan approved with standard interest rate")
    else:
        print("Loan rejected: Requested amount exceeds eligibility")
