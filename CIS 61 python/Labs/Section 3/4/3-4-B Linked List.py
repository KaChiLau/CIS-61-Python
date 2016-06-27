class HonorRoll:
    def __init__(self, aName, FirstNType):
        self.Name = aName
        self.BasePairs = 1
        print("Student",self.Name,"constructed.\n") # Remove after Testing
        self.CurrentNT = self.FirstNT = Student(FirstNType)

    def AddNT(self,NType):
        self.FindEnd()
        self.CurrentNT.NextNT = Student(NType)
        self.BasePairs += 1
        self.CurrentNT = self.CurrentNT.NextNT
        return self.CurrentNT

    def FindEnd(self):
        while self.CurrentNT.NextNT:
            self.CurrentNT = self.CurrentNT.NextNT
        return self.CurrentNT
        
    def Display(self):
        print("Letter", self.Name, self.BasePairs, "Students:")
        self.CurrentNT = self.FirstNT
        self.FirstNT.Display()
        while(self.CurrentNT.NextNT):
            self.CurrentNT = self.CurrentNT.NextNT
            self.CurrentNT.Display()

class Student:
    def __init__(self,Symbol):
        self.Symbol = Symbol
        if (Symbol == 'H'):
            self.Name = "Helen"
            self.Mass = 135.13 # g/mol
        elif (Symbol == 'O'):
            self.Name = "Osis"
            self.Mass = 111.10 # g/mol
        elif (Symbol == 'N'):
            self.Name = "Ning"
            self.Mass = 151.13 # g/mol
        elif (Symbol == 'R'):
            self.Name = "Ray"
            self.Mass = 126.11 # g/mol
        elif (Symbol == 'L'):
            self.Name = "Linda"
            self.Mass = 126.11 # g/mol
        self.NextNT = None
        # print("Here I am!", self.Name) # Remove after Testing
        
    def Display(self):
        print(self.Symbol,self.Name,self.Mass)

# The TEST HARNESS
Norma = HonorRoll("Honor Roll", 'H')
Norma.AddNT('O')
Norma.AddNT('N')
Norma.AddNT('O')
Norma.AddNT('R')
Norma.AddNT('R')
Norma.AddNT('O')
Norma.AddNT('L')
Norma.AddNT('L')
Norma.Display()
