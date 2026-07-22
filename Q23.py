print("-----HOSPITAL DIAGNOSIS-----\n")


fever=input("Do you have fever? (yes/no)\n").lower()
cough=input("Do you have cough? (yes/no)\n").lower()
headache=input("Do you have headache? (yes/no)\n").lower()
breathing=input("Do you have breathing problem? (yes/no)\n").lower()


if breathing=="yes":
    print("Emergency! Visit Hospital Immediately")


elif fever=="yes" and cough=="yes" and headache=="yes":
    print("Possible Flu")


elif cough=="yes" and fever=="no":
    print("Possible Cold")


else:
    print("No Serious Symptoms Detected")