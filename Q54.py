print("-----ONLINE EXAM PROCTOR-----\n")

faceDetected = input("Is your face visible in camera? (yes/no):\n").lower()

if faceDetected == "no":
    print("Warning issued: Face not visible")
else:
    tabSwitches = int(input("Enter number of tab switches detected:\n"))
    if tabSwitches == 0:
        print("No violations detected")
    elif tabSwitches <= 2:
        print("Warning: Suspicious activity logged")
    else:
        multiplePeople = input("Was more than one person detected? (yes/no):\n").lower()
        if multiplePeople == "yes":
            print("Exam terminated: Malpractice detected")
        else:
            print("Exam flagged for manual review")
