print("-----CHEMICAL LAB EXPERIMENT-----\n")


chemical=input("Chemical type (safe/dangerous)\n").lower()
temperature=int(input("Enter Temperature\n"))
pressure=int(input("Enter Pressure\n"))


if chemical=="dangerous" and temperature>100 and pressure>80:
    print("Explosion Warning! Shut Down Lab")


elif temperature>100 or pressure>80:
    print("Dangerous Reaction Detected")


elif chemical=="safe" and temperature>=20 and temperature<=100 and pressure<80:
    print("Experiment Successful")


else:
    print("Experiment Failed")