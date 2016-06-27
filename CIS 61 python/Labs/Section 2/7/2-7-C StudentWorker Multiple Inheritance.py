class Work(object):

    studentW = "Providing Information to students"
    workerW = "Cleaning"
    def __init__(self):
        return

class Student(Work):
    i = 'student'
    def Name(self, name):
        print("Name: ", name)
    def ID(self, iD):
        print("ID: ", iD)
    def Job(self, work):
        print("Work: ", Work.studentW)

class Worker(Work):
    i = 'worker'
    def Name(self, name):
        print("Name: ", name)
    def ID(self, iD):
        print("ID: ", iD)
    def Job(self, work):
        print("Work: ", Work.workerW)

class College(Student, Worker):
    def print(self, something):
        print("We have", Student.i, "and", Worker.i, "to help us for the works in our college")


S = Student()
S.Name('Tom')
S.ID('1099999')
S.Job('Let see')

print(' ')

W = Worker()
W.Name('Ken')
W.ID('1099889')
W.Job('Let see')

print(' ')
C = College()
C.print('Tom')
