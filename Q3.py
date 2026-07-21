age=int(input("ENter your age\n"))
monthlyIncome=int(input("Enter your monthly income\n"))
creditScore=int(input("Enter your credit score\n"))
existingLoan=int(input("How many existing loan you have?\n"))

if age <18:
    print("Loan Rejected, You must be 18 or older")

elif monthlyIncome <3000:
    print("Loan Rejected, minimum monthly income must be 3000$ or more")

elif creditScore <700:
    print("Loan Rejected, Your credit score is low")

elif existingLoan >2:
    print("Loan Rejected, Too many existing loan")

else:
    print("Loan Approved")