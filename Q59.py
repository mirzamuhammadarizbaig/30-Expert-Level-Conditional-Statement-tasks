print("-----STOCK MARKET ALERT SYSTEM-----\n")

stockPrice = int(input("Enter current stock price:\n"))
avgPrice = int(input("Enter your average buying price:\n"))
volume = int(input("Enter today's trading volume:\n"))

if stockPrice > avgPrice:
    change = ((stockPrice - avgPrice) / avgPrice) * 100
    if change >= 10 and volume > 1000000:
        print("Strong BUY momentum, consider holding for more gains")
    elif change >= 10:
        print("Price rising but low volume, trade cautiously")
    else:
        print("Minor gain, hold your position")

elif stockPrice < avgPrice:
    change = ((avgPrice - stockPrice) / avgPrice) * 100
    if change >= 15:
        print("Alert: Significant drop, review your position")
    else:
        print("Minor dip, no action needed")

else:
    print("No change in price")
