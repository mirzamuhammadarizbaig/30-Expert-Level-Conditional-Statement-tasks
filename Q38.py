print("-----EXAM GRADING SYSTEM-----\n")

marks = int(input("Enter your marks out of 100:\n"))
attendance = int(input("Enter your attendance percentage:\n"))

if attendance < 75:
    print("You are not eligible to receive a grade due to low attendance")
else:
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Your grade is:", grade)

    if grade == "F":
        print("You need to reappear for the exam")
    elif grade == "A+" or grade == "A":
        print("Excellent performance!")
