def check(e):
    while((e < 0) | (e > 101)):
            e = int(input("Please re-enter:"))
    return

def average(e1, e2, e3, e4, e5, e6, e7):
    return (e1 + e2 + e3 + e4 + e5 + e6 + e7) / 7

e1 = int(input("Please Enter Your 1st exam score: "))
check(e1)
e2 = int(input("Please Enter Your 2nd exam score: "))
check(e2)
e3 = int(input("Please Enter Your 3rd exam score: "))
check(e3)
e4= int(input("Please Enter Your 4th exam score: "))
check(e4)
e5 = int(input("Please Enter Your 5th exam score: "))
check(e5)
e6 = int(input("Please Enter Your 6th exam score: "))
check(e6)
e7 = int(input("Please Enter Your 7th exam score: "))
check(e7)

print("The Average: ", average(e1, e2, e3, e4, e5, e6, e7))
