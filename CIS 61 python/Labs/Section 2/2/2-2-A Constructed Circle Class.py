pi = 3.1415

class Circle:
    def __init__(self, Radius): #Constructor 
        self.Radius = Radius
        self.Circumference = 2 * pi * self.Radius
        self.Area = pi * (Radius ** 2)
        self.Diameter = 2 * Radius
    """
    def Circumference(self):
        return 2 * pi * self.Radius
    def Area(self):
        return pi * (Radius ** 2)
    def Diameter(self):
        return 2 * Radius
    """

"""input something from outside, then use it inside"""

"""for the constructor, it's __, not _"""

C = Circle(5)

A = C.Area
print("Area is", A)
Cir = C.Circumference
print("Circumference is", Cir)
D = C.Diameter
print("Circumference is", D)
