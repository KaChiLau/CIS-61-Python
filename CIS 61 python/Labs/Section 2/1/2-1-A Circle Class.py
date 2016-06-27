pi = 3.1415

class Circle:
    def circumference(radius):
        return 2 * pi * radius
    def area(radius):
        return pi * (radius ** 2)
    def diameter(radius):
        return 2 * radius
c = Circle

x = c.circumference(3.9)
print("circumference: ", x)

y = c.area(3.9)
print("area: ", y)

z = c.diameter(3.9)
print("diameter: ", z)
