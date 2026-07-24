print("-----SMART WATCH HEALTH MONITOR-----\n")

heartRate = int(input("Enter current heart rate (bpm):\n"))
steps = int(input("Enter steps taken today:\n"))

if heartRate > 100:
    activity = input("Are you currently exercising? (yes/no):\n").lower()
    if activity == "yes":
        print("Heart rate elevated due to exercise, normal")
    else:
        print("Warning: High resting heart rate detected, consult a doctor")

elif heartRate < 60:
    print("Warning: Low heart rate detected")
else:
    print("Heart rate is normal")

if steps >= 10000:
    print("Daily step goal achieved!")
elif steps >= 5000:
    print("Good progress, keep moving")
else:
    print("Try to walk more today")
