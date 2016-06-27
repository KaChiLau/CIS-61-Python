"""
Ka Chi Lau
1-4-C Shipping Charge
"""

def shipping(p):
    fcharge = 0.00
    pcharge = 1.99
    return p * pcharge 

p = int(input("# of book: "))

print("total charge: ", shipping(p))
