"""
Ka Chi Lau
1-6-B Triangles’ Angles
"""

def addDegrees(a1, b1, c1, m):

    return a1 + b1 + c1 + m

def addMinutes(a2, b2, c2, s):

    temp = a2 + b2 + c2 + s

    i = 0
    if(temp == 60):
        i += 1
    elif(temp > 59):
        while(temp > 59):
            i += 1
            temp = temp - 60
    return i

def addSeconds(a3, b3, c3):

    temp = a3 + b3 + c3

    i = 0
    if(temp == 60):
       i += 1
    elif(temp > 59):
        while(temp > 59):
            i += 1
            temp = temp - 60
    return i

def reduceSeconds(a3, b3, c3):

    s = a3 + b3 + c3

    if(s == 60):
        s = 0
    elif(s > 59):
        while(s > 59):
            s = s - 60
    return s

def reduceMinutes(a2, b2 , c2, s):

    m = a2 + b2 + c2 + s

    if(m == 60):
        m = 0
    elif(m > 59):
        while(m > 59):
            m = m - 60        
    return m

def defineAngle(d, m, s):

    a = 'Euclidean'
    b = 'Elliptical'
    c = 'Hyperbolic'

    if(d > 180):
        return b
    elif(d < 180):
        return c
    else:
        if(d == 180) & (m == 0) & (s == 0):
            return a
        elif(d == 180) | (m > 0):
             return b
        elif(d == 180) | (s > 0):
             return b
    return

a1 = int(input("Please enter the 1st angle's degrees: "))
a2 = int(input("Please enter the 1st angle's minutes: "))
a3 = int(input("Please enter the 1st angle's second: "))
b1 = int(input("Please enter the 2nd angle's degrees: "))
b2 = int(input("Please enter the 2nd angle's minutes: "))
b3 = int(input("Please enter the 2nd angle's second: "))
c1 = int(input("Please enter the 3rd angle's degrees: "))
c2 = int(input("Please enter the 3rd angle's minutes: "))
c3 = int(input("Please enter the 3rd angle's second: "))

s = addSeconds(a3, b3, c3)

m = addMinutes(a2, b2, c2, s)

d = addDegrees(a1, b1, c1, m)

m = reduceMinutes(a2, b2, c2, s)

s = reduceSeconds(a3, b3, c3)


if (a1 + a2 + a3) == (b1 + b2 + b3) == (c1 + c2 + c3):
   print(defineAngle(d, m, s), "Equilateral Triangle")

elif (a1 + a2 + a3) == (b1 + b2 + b3) != (c1 + c2 + c3):
    print(defineAngle(d, m, s), "Isosceles Triangle")

elif (b1 + b2 + b3) == (c1 + c2 + c3) != (a1 + a2 + a3):
    print(defineAngle(d, m, s), "Isosceles Triangle")

elif (c1 + c2 + c3) == (a1 + a2 + a3) != (b1 + b2 + b3):
    print(defineAngle(d, m, s), "Isosceles Triangle")
    
else:
    print(defineAngle(d, m, s), "Scalene Triangle")


print("Total Angle: ", d, m, s)
"""
http://learnpythonthehardway.org/book/ex33.html
"""

