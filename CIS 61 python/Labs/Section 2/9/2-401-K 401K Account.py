from datetime import datetime

class Tax:
    def __init__(self, name, birthdayYear): #Constructor
        self.name = name
        self.birthdayYear = birthdayYear
    def Tname(self):
        return self.name
    def Tyear(self):

        currentYear = datetime.now().year
        if (currentYear - self.birthdayYear) < 59:
            return 'tax penalities'
        else:
            return 'Good'


pname = []
byear = []
taxP = []

option = 0
while option != 2:
    option = int(input("1)withdrawals\n2)quit\nplease select options: "))

    if option == 1:
        name = str(input("Fullname: "))
        birthday = int(input("birthdayYear: "))
        T = Tax(name, birthday)
        pname.append(T.Tname())
        byear.append(birthday)
        taxP.append(T.Tyear())

print("name: ", pname)
print("Birthday: ", byear)
print("tax status: ", taxP)
