print("-----GYM MEMBERSHIP PLAN-----\n")

age = int(input("Enter your age:\n"))

if age < 16:
    print("Sorry, you must be at least 16 to join")
else:
    plan = input("Choose plan (Basic/Premium/VIP):\n").lower()

    if plan == "basic":
        print("Membership fee: 3000/month")
    elif plan == "premium":
        print("Membership fee: 5000/month")
        trainer = input("Do you want a personal trainer? (yes/no):\n").lower()
        if trainer == "yes":
            print("Additional 2000 for trainer, total: 7000/month")
    elif plan == "vip":
        print("Membership fee: 10000/month")
        print("Includes personal trainer and diet plan")
    else:
        print("Invalid plan selected")
