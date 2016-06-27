"""
a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
c = int(input("Please enter c: "))
t = a, b, c

print(t)
"""

a1 = int(input("Please enter a: "))
a2 = int(input("Please enter a: "))
a3 = int(input("Please enter a: "))
b1 = int(input("Please enter b: "))
b2 = int(input("Please enter b: "))
b3 = int(input("Please enter b: "))
c1 = int(input("Please enter c: "))
c2 = int(input("Please enter c: "))
c3 = int(input("Please enter c: "))
d1 = int(input("Please enter d: "))
d2 = int(input("Please enter d: "))
d3 = int(input("Please enter d: "))
e1 = int(input("Please enter e: "))
e2 = int(input("Please enter e: "))
e3 = int(input("Please enter e: "))

a = a1 + b1 + c1 + d1 + e1
b = a2 + b2 + c2 + d2 + e2
c = a3 + b3 + c3 + d3 + e3

t = a, b, c

print("\n\t#\t\t2H\tht\t2T")

print("\tTrial 1:", '\t' ,a1, '\t' ,a2, '\t' ,a3)
print("\tTrial 2:", '\t' ,b1, '\t' ,b2, '\t' ,b3)
print("\tTrial 3:", '\t' ,c1, '\t' ,c2, '\t' ,c3)
print("\tTrial 4:", '\t' ,d1, '\t' ,d2, '\t' ,d3)
print("\tTrial 5:", '\t' ,e1, '\t' ,e2, '\t' ,e3)

print("\n\tThe total of the trials is: ", t)
