pin=1212009
balance=1000000

pinEnter=input("Enter your pin:\n")

if pinEnter==str(pin):
    print("Welcome to your account Ariz Baig")
    print("Your balance is:",balance)
    
    choice=input("Enter your choice (1 for withdraw, 2 for deposit):\n")
    if choice=="1":
        withdrawCash=int(input("Enter the amount you want to withdraw:\n"))
        if withdrawCash<balance:
            print("Succesfully withdraw",withdrawCash)

        else:
            print("Insufficient amount")

    if choice=="2":
        depositCash=int(input("Enter the amount you want to deposit\n"))
        if depositCash>0:
            newBalance=balance+depositCash
            print("Succesfully Deposit", depositCash)
            print("Your new account balance is", newBalance)

else:
    print("Incorrect pin. Please try again.")