print("-----MOVIE TICKET BOOKING-----\n")

age = int(input("Enter your age:\n"))
movie = input("Choose movie category (Action/Horror/Kids):\n").lower()

if movie == "action":
    if age >= 18:
        print("Booking confirmed for Action movie")
        seat = input("Choose seat type (VIP/Normal):\n").lower()
        if seat == "vip":
            print("Ticket price: 1500")
        elif seat == "normal":
            print("Ticket price: 800")
        else:
            print("Invalid seat type")
    else:
        print("You must be 18+ to watch this movie")

elif movie == "horror":
    if age >= 15:
        print("Booking confirmed for Horror movie")
    else:
        print("You must be at least 15 to watch this movie")

elif movie == "kids":
    print("Booking confirmed for Kids movie")
    if age > 12:
        print("Note: This movie is best for kids under 12")

else:
    print("Invalid movie category")
