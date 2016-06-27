from datetime import datetime

class Book:
    def __init__(self, name, iD): #Constructor
        self.name = name
        self.iD = iD
    def Bname(self):
        return self.name
    def BiD(self):
        return self.iD
    def Btime(self):
        return str(datetime.now())

bookname = []
studentID = []
time = []

option = 0
while option != 2:
    option = int(input("1)lend\n2)quit\nplease select options: "))

    if option == 1:
        name = str(input("Fullname: "))
        iD = int(input("ID: "))
        B = Book(name, iD)
        bookname.append(B.Bname())
        studentID.append(B.BiD())
        time.append(B.Btime())
        

print("bookname: ", bookname)
print("ID: ", studentID)
print("Time: ", time)
