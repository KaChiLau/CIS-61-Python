class College:
    def __init__(self, Fullname, Shortname, Address): #Constructor
        self.Fullname = Fullname
        self.ShortName = Shortname
        self.Address = Address
    def Full(self):
        return self.Fullname
    def Short(self):
        return self.ShortName
    def Adr(self):
        return self.Address

fullname = str(input("Fullname: "))
shortname = str(input("Shortname: "))
while len(shortname) > 10:
    shortname = str(input("please re-input the shortname"))
    
address = str(input("Address: "))

C = College(fullname, shortname, address)

F = C.Full()
print("Full name: ", F)

S = C.Short()
print("Short name ", S)

A = C.Adr()
print("Address ", A)
