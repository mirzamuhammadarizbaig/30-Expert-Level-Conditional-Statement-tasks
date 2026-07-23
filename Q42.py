print("-----INSURANCE CLAIM APPROVAL-----\n")

policyActive = input("Is your policy currently active? (yes/no):\n").lower()

if policyActive == "yes":
    claimAmount = int(input("Enter claim amount:\n"))
    yearsWithCompany = int(input("Enter number of years with the company:\n"))

    if claimAmount <= 50000:
        print("Claim approved instantly")
    elif claimAmount <= 200000:
        if yearsWithCompany >= 2:
            print("Claim approved after verification")
        else:
            print("Claim sent for manual review")
    else:
        if yearsWithCompany >= 5:
            print("Claim approved after manual review")
        else:
            print("Claim rejected, insufficient policy history for this amount")
else:
    print("Claim denied, policy is not active")
