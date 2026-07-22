print("-----SCHOLARSHIP ELIGIBILITY-----\n")

marks=float(input("Enter your percentage\n"))
income=int(input("Enter your family income\n"))
attendance=float(input("Enter your attendance percentage\n"))

if marks>=90 and income<50000 and attendance>=80:
    print("Scholarship Approved")

elif marks>=80 and attendance>=80:
    print("Partial Scholarship")

else:
    print("Scholarship Rejected")