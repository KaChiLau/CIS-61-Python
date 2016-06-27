"""
ary = [[1,2]]


myArray[0][1] = 234

print(ary[0][0])

print(ary[0][1])

ary[0][0] = 1
ary[0][1] = 1

print(myArray[0][1])
"""

myArray=[[0 for j in range(5)] for i in range(7)]

myArray[0][0] = 2725
myArray[0][1] = 2974
myArray[0][2] = 3088
myArray[0][3] = 3239
myArray[0][4] = 3357

myArray[1][0] = 2357
myArray[1][1] = 2594
myArray[1][2] = 2708
myArray[1][3] = 2819
myArray[1][4] = 2935

myArray[2][0] = 2159
myArray[2][1] = 2304
myArray[2][2] = 2416
myArray[2][3] = 2530
myArray[2][4] = 2707

myArray[3][0] = 1980
myArray[3][1] = 2081
myArray[3][2] = 2194
myArray[3][3] = 2305
myArray[3][4] = 2403

myArray[4][0] = 1787
myArray[4][1] = 1900
myArray[4][2] = 2015
myArray[4][3] = 2015
myArray[4][4] = 2015

myArray[5][0] = 1700
myArray[5][1] = 1700
myArray[5][2] = 1700
myArray[5][3] = 1700
myArray[5][4] = 1700

myArray[6][0] = 1516
myArray[6][1] = 1516
myArray[6][2] = 1516
myArray[6][3] = 1516
myArray[6][4] = 1516

x = int(input("Please Enter your Grade: \n1)E-7\n2)E-6\n3)E-5\n4)E-4\n5)E-3\n6)E-2\n7)E-1\n"))
y = int(input("Please Enter your Years of Service: \n1)Less than 2\n2)Over 2\n3)Over 3\n4)Over 4\n5)Over 6\n"))

if x == 1 & y == 1:
    print(" The rate is",  myArray[0][0])
elif (x == 1) & (y == 2):
    print(" The rate is", myArray[0][1])
elif (x == 1) & (y == 3):
    print(" The rate is", myArray[0][2])
elif (x == 1) & (y == 4):
    print(" The rate is", myArray[0][3])
elif (x == 1) & (y == 5):
    print(" The rate is", myArray[0][4])
elif (x == 2) & (y == 1):
    print(" The rate is", myArray[1][0])
elif (x == 2) & (y == 2):
    print(" The rate is", myArray[1][1])
elif (x == 2) & (y == 3):
    print(" The rate is", myArray[1][2])
elif (x == 2) & (y == 4):
    print(" The rate is", myArray[1][3])
elif (x == 2) & (y == 5):
    print(" The rate is", myArray[1][4])
elif (x == 3) & (y == 1):
    print(" The rate is", myArray[2][0])
elif (x == 3) & (y == 2):
    print(" The rate is", myArray[2][1])
elif (x == 3) & (y == 3):
    print(" The rate is", myArray[2][2])
elif (x == 3) & (y == 4):
    print(" The rate is", myArray[2][3])
elif (x == 3) & (y == 5):
    print(" The rate is", myArray[2][4])
elif (x == 4) & (y == 1):
    print(" The rate is", myArray[3][0])
elif (x == 4) & (y == 2):
    print(" The rate is", myArray[3][1])
elif (x == 4) & (y == 3):
    print(" The rate is", myArray[3][2])
elif (x == 4) & (y == 4):
    print(" The rate is", myArray[3][3])
elif (x == 4) & (y == 5):
    print(" The rate is", myArray[3][4])
elif (x == 5) & (y == 1):
    print(" The rate is", myArray[4][0])
elif (x == 5) & (y == 2):
    print(" The rate is", myArray[4][1])
elif (x == 5) & (y == 3):
    print(" The rate is", myArray[4][2])
elif (x == 5) & (y == 4):
    print(" The rate is", myArray[4][3])
elif (x == 5) & (y == 5):
    print(" The rate is", myArray[4][4])
elif (x == 6) & (y == 1):
    print(" The rate is", myArray[5][0])
elif (x == 6) & (y == 2):
    print(" The rate is", myArray[5][1])
elif (x == 6) & (y == 3):
    print(" The rate is", myArray[5][2])
elif (x == 6) & (y == 4):
    print(" The rate is", myArray[5][3])
elif (x == 6) & (y == 5):
    print(" The rate is", myArray[5][4])
elif (x == 7) & (y == 1):
    print(" The rate is", myArray[6][0])
elif (x == 7) & (y == 2):
    print(" The rate is", myArray[6][1])
elif (x == 7) & (y == 3):
    print(" The rate is", myArray[6][2])
elif (x == 7) & (y == 4):
    print(" The rate is", myArray[6][3])
elif (x == 7) & (y == 5):
    print(" The rate is", myArray[6][4])
else:
    print("You enter incorrect data")
    
