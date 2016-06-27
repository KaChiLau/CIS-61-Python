"""
Ka Chi Lau
1-5-B Quadratic Discriminant
"""

def quadratic(a, b, c):
    if a == 0:
        print("you can’t use the formula.")

    elif ((b**2) - 4 * a * c) < 0:
        print("There is no solution")
    
    else:
        x1 = (-b + ((b**2) - 4 * a * c) **(1/2))/ (2 * a)
        x2 = (-b - ((b**2) - 4 * a * c) **(1/2))/ (2 * a)

        print("x = ", x1 , "x = ", x2)

    return

a = int(input("Please Enter the value of a: "))
    
b = int(input("Please Enter the value of b: "))

c = int(input("Please Enter the value of c: "))

quadratic(a, b, c)
