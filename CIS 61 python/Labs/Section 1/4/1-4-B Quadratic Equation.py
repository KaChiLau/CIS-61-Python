"""
KaChiLau
1-4-B Quadratic Equation
"""


a = 3

b = 4

c = 5

x = 2

def Quadratic (a, b, c, x):

    y = a * (x ** 2) + b * x + c

    return y

print("y = ", Quadratic(a, b, c, x))
