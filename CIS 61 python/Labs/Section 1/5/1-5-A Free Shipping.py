"""
Ka Chi Lau
1-5-A Free Shipping?
"""

def free(price):
    if price > 50:
        print("Your shipping is free")
    else:
        print("Sorry, your shipping balance couldn't reach our free shipping requirement")
    return


price = int(input("Please Enter a price: $"))

free(price)

