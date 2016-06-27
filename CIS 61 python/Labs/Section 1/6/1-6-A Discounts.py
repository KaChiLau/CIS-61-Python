def discount(total):

    if (total > 50) & (total < 100):
        temp = ((5/100) * total)
        final = total - temp
    elif (total > 100) & (total < 500):
        temp = ((10/100) * total)
        final = total - temp
    elif (total > 500):
        temp = ((15/100) * total)
        final = total - temp
    else:
        print("Sorry, your amount of of purchase couldn't reach our discounts requirement")
        return

    print("The price after discount: $", final)

    return

total = float(input("Please enter the amount of your purchase: $"))

discount(total)
