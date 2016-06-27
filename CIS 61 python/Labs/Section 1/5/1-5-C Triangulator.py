"""
Ka Chi Lau
1-5-C Triangulator?
"""

def triangle(a, b, c) :
    if (a == b) & (b == c) & (c == a):
        print("It is an equilateral triangle.")
    elif (a == b) | (b == c) | (c == a):
        print("It is an isosceles triangle.")
    elif (a + b + c) < max(a,b,c) * 2:
        print("“Shame on you, that is not a triangle!”")
    else:
        print("It's valid")
    return

a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))
        
triangle(a,b,c)
