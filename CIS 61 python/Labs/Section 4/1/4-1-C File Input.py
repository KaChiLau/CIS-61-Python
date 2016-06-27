class Employee:
    def __init__(self, Name, Address):
        self.Name = Name
        self.Address = Address
    def Display(self):
        print(self.Name, self.Address)

Pat = Employee('Pat', 'Oakland')
Lily = Employee('Lily', 'San Francisco')
Bill = Employee('Bill', 'San Diego')

EmployeeList = [Pat, Lily, Bill]

TheFile = open('EmployeeFile.txt', 'w') # 'w' for WRITE

for s in range(0, len(EmployeeList)):
    TheFile.write(format(EmployeeList[s].Name, '10s'))
    TheFile.write(format(str(EmployeeList[s].Address),'20s'))

TheFile.close()

TheFile = open('EmployeeFile.txt')

TheList = []

Name = TheFile.read(5)

while Name != "":
    Address = str(TheFile.read(5))
    TheList.append(Employee(Name,Address))
    Name = TheFile.read(10)

for s in range(0, len(TheList)):
    TheList[s].Display()
