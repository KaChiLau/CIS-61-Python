"""OUTPUT
>>> ================================ RESTART ================================
>>> 
please the value of a: 3
please the value of b: 4
please the value of c: 5
The Area is:  6.0
>>> 
"""

a = int(input("please the value of a: "))

b = int(input("please the value of b: "))

c = int(input("please the value of c: "))

s = (a + b + c)/2

area = (s * (s - a) * (s - b) * (s - c)) ** (1/2)

print("The Area is: ", area)

