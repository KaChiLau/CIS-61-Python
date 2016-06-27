class MotorVehicle(object):
    i = "This is a MotorVehicle"
    def __init__(self):
        return

class Car(MotorVehicle):
    i = 'Car'
    def system(self, motorVehicle):
        print("Class Car--\n", MotorVehicle.i)
        return
        
class Truck(MotorVehicle):
    i = 'Truck'
    def system(self, motorVehicle):
        print("Class Truck--\n", MotorVehicle.i)
        return

class MotorCycle(MotorVehicle):
    i = 'MotorCycle'
    def system(self, motorVehicle):
        print("Class MotorCycle--\n", MotorVehicle.i)
        return

class Bicycle(MotorVehicle):
    i = 'Bicycle'
    def system(self, motorVehicle):
        print("Class Bicycle--\n", MotorVehicle.i)
        return

class AllmotorVehicle(Car, Truck, MotorCycle, Bicycle):
    def __init__(self):
        return
    def print(self, something):
        print("All MotorVehicle: ", Car.i, ',', Truck.i, ',', MotorCycle.i, ',', Bicycle.i)

C = Car()
C.system('tom')

T = Truck()
T.system('tom')

M = MotorCycle()
M.system('tom')

B = Bicycle()
B.system('tom')

All = AllmotorVehicle()
All.print('tom')
