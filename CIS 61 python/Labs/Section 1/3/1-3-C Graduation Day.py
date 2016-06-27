"""
KaChiLau
1-3-C Graduation Day?
"""

transferU = int(input("how many units they have in transfer: "))

years = int(input("please enter how many years of military/public service: "))

usingU = int(input("how many units they have in using: "))

totalU = 125 - (usingU + min(transferU, 25) + min(years * 5, 15))

"""min(T, 25) IF T > 25, it will pick 25""" 

print("how many units they have toward graduation: ", totalU)
print("how many total until you have: ", (usingU + min(transferU, 25) + min(years * 5, 15)))
70
