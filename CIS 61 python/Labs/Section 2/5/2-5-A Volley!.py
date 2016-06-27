class Team:
    def __init__(self, teamName):
        self.teamName = teamName
    def team(self):
        return self.teamName
    def Plist(self):
        x = []
        y = 0
        while(y < 6):
            c = str(input("Enter name: "))
            x.append(c)
            y += 1
        return x
    def color(self):
        y = []
        z = 0
        while(z < 2):
            o = str(input("Enter colors: "))
            y.append(o)
            z += 1
        return y


teamlist = []


i = 0
k = 0
while i < 2:
    teamName = str(input("Fullname: "))
    T = Team(teamName)
    P = T.Plist()
    C = T.color()
    teamlist.append(teamName)
    k += 1
    teamlist.append(C)
    k += 1
    teamlist.append(P)
    k += 1

    i += 1

i = 0
k = 3
while i < 2:
    if i == 1:
        print(teamlist[0:k])
        k += 3
        i += 1
    else:
        print(teamlist[k:])
        i += 1
    

