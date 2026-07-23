print("-----CRYPTO TRADING BOT-----\n")

currentPrice = int(input("Enter current coin price:\n"))
buyPrice = int(input("Enter your buying price:\n"))
coinsHeld = int(input("Enter number of coins held:\n"))

profit = (currentPrice - buyPrice) * coinsHeld

if currentPrice > buyPrice:
    profitPercent = ((currentPrice - buyPrice) / buyPrice) * 100
    if profitPercent >= 20:
        print("Strong SELL signal, profit:", profit)
    elif profitPercent >= 5:
        print("Consider selling, profit:", profit)
    else:
        print("Hold, small profit:", profit)

elif currentPrice < buyPrice:
    lossPercent = ((buyPrice - currentPrice) / buyPrice) * 100
    if lossPercent >= 20:
        print("Strong SELL signal to cut losses, loss:", -profit)
    else:
        print("Hold, minor loss:", -profit)

else:
    print("No profit, no loss. Hold your position")
