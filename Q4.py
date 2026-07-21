print("\n-----UNIVERSITY OF MITI-----")



math=float(input("Enter your Math number\n"))
english=float(input("Enter your English number\n"))
science=float(input("Enter your Science number\n"))
interview=input("Did you gave the interview\n")

average=(math+english+science)/3

if math <60:
    print("Math score is below 60, REJECTED!")

elif english <60:
    print("English score is below 60, REJECTED!")

elif science <60:
    print("Science score is below 60, REJECTED!")

elif interview=="no":
    print("Waitlisted!")

elif average<75:
    print("Your Average score is below 75, Waitlisted")

else:
    print("Congratulations you are Accepted")

