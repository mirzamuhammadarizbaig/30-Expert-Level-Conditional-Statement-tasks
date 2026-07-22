print("-----CREDIT CARD APPROVAL-----\n")

age=int(input("Enter your age\n"))
income=int(input("Enter your monthly income\n"))
creditScore=int(input("Enter your credit score\n"))

if age>=18 and income>=50000 and creditScore>=700:
    print("Credit Card Approved")

elif income>=30000 and creditScore>=650:
    print("Needs Further Verification")

else:
    print("Credit Card Rejected")