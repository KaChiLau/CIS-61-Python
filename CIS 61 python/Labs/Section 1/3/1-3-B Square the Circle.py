"""
KaChiLau
1-3-B Square the Circle
"""


from math import sqrt, exp

pi = 3.14159

r = float(input("please the value of radius: "))

areaC = pi * (r**2)

print("Area of cirlce: ", areaC)

areaS = areaC

"""SideS = areaS ** (1/2)"""

SideS = sqrt(areaS)

print("Side of the length of a square: ", SideS)
