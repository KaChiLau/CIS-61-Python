class Major:
    def __init__(self, name):
        self.Name = name
    def print(self):
        print("Major", self.Name)
        
class Student:
    def __init__(self, name):
        self.Name = name
    def print(self):
        print("Student", self.Name)

class System:
    def __init__(self, student, major):
        self.Student = student
        self.Major = major
    def printDot(self):
        print("Student: ",self.Student.Name,
              "\nMajor: ", self.Major.Name)

S = Student("Ken")
M = Major("CIS")
Sys = System(S, M)
Sys.printDot()
