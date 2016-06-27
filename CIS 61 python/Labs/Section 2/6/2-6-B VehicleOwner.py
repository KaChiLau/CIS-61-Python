class VehicleType:
    def __init__(self, vtype):
        self.Type = vtype
    def print(self):
        print("Vehicle", self.Type)
        
class Vehicle:
    def __init__(self, iD, vehicleType):
        self.ID = iD
        self.VehicleType = vehicleType
    def print(self):
        print("Vehicle", self.ID)
    def print(self):
        print("Vehicle", self.VehicleType.Type)
        
class OwnerID:
    def __init__(self, iD):
        self.ID = iD
    def print(self):
        print("Vehicle", self.ID)
        
class Owner:
    def __init__(self, name, ownerID):
        self.Name = name
        self.OwnerID = ownerID
    def print(self):
        print("Owner", self.Name)
    def print(self):
        print("ID", self.OwnerID.ID)

class System:
    def __init__(self, owner, vehicle):
        self.Owner = owner
        self.Vehicle = vehicle
    def printDot(self):
        print("Owner: ",self.Owner.Name)
        print("OwnerID: ", self.Owner.OwnerID.ID)
        print("VehicleID: ", self.Vehicle.ID)
        print("VehicleType: ", self.Vehicle.VehicleType.Type)


VT = VehicleType("Honda")
V = Vehicle("108VH96", VT)
OI = OwnerID("7777777")
O = Owner("Ken", OI)
Sys = System(O, V)
Sys.printDot()
