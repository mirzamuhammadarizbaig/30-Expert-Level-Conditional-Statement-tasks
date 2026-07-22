print("-----DETECTIVE INVESTIGATION SYSTEM-----\n")

fingerprint=input("Did you find a fingerprint? (yes/no)\n").lower()
cctv=input("Is CCTV footage available? (yes/no)\n").lower()
witness=input("Is there a witness? (yes/no)\n").lower()
alibi=input("Does the suspect have an alibi? (yes/no)\n").lower()


if fingerprint=="yes" and alibi=="no":
    print("Prime Suspect")

elif cctv=="yes" and witness=="yes":
    print("Strong Evidence Found")

elif alibi=="yes":
    print("Needs More Investigation")

else:
    print("Not Enough Evidence")