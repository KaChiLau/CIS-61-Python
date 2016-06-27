class California(object):
    i = 'California'
    def __init__(self):
        return

class CommunityCollege(California):
    i = 'Community college'
    def system(self, california):
        print(California.i)
        return
        
class MajorArea(CommunityCollege):
    i = 'MajorArea'
    def system(self, communityCollege):
        print(CommunityCollege.i)
        return

class CIS(MajorArea):
    i = 'CIS'
    def system(self, majorArea):
        print(MajorArea.i)
        return

CC = CommunityCollege()
CC.system('tom')

MA = MajorArea()
MA.system('tom')

C = CIS()
C.system('tom')

print(C.i)
