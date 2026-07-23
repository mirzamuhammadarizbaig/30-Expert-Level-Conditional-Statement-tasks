print("-----JOB INTERVIEW SCREENING-----\n")

experience = int(input("Enter years of experience:\n"))
skillTest = int(input("Enter skill test score out of 100:\n"))

if skillTest < 40:
    print("Rejected: Skill test score too low")
else:
    if experience >= 5:
        print("Shortlisted for Senior position")
    elif experience >= 2:
        if skillTest >= 70:
            print("Shortlisted for Mid-level position")
        else:
            print("Shortlisted for Junior position")
    else:
        if skillTest >= 80:
            print("Shortlisted for Junior position (exceptional test score)")
        else:
            print("Rejected: Insufficient experience")
