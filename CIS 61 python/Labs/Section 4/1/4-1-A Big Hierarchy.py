class Family:
    def __init__(self):
        self.Tree = 0
    def Display(self):
        print("\n\tFamily Tree")

class Grand(Family):
    def __init__(self):
        self.Grand = 1
    def Display(self):
        super().Display()
        print("\n\tGrand")

class Parent(Grand):
    def __init__(self):
        self.Parent = 2
    def Display(self):
        super().Display()
        print("\n\tParent")

class Me(Parent):
    def __init__(self, Name):
        self.Name = Name

    def Display(self):
        print("ALl about", self.Name)
        super().Display()
        print("\n\tMe <--")

Lau = Me("My Family")

Lau.Display()
