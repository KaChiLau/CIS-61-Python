Products = { 'Coke': 2.00, 'Lemon Coke': 2.25, 'Special Coke': 3.00}

class Coin:
    Values = { 'Nickle': 0.05,
               'Dime': 0.10,
               'Quaters': 0.25,
               'Dollars': 1.00,
               '10Dollars': 10.00,
               '20Dollars': 20.00 }

    def __init__(self, C):
        self.Value = Coin.Values[C]
    
    def Display(self):
        print("Coins: ", self.Value)

class Active:
    def __init__(self):
        self.Running = False
        self.Light = "Off"
    def On(self):
        self.Running = True
        self.Light = "On"
    def Off(self):
        self.Running = False
        self.Light = "Off"
    def Display(self):
        print("The Machines is on/off")

class CoinReturn(Active):

    def Return(self):
        Active.Off()
    
    def Display(self):
        print("Here is your coin")

class Selection:
    def __init__(self):
        self.Option = 0
        
class System:

    def __init__(self):
        self.total = 0.00
        self.product = 0
        return
    
    def InsertCoin(self, coin):
        self.total += coin.Value

    def ReturnCoin(self):
        if self.total >= 0:
            CoinReturn()
            self.total = 0
    def Select(self, option):
        self.product = Products['Coke']

    def Deliver(self):
        print(self.product)
        
Coke = System()
Coke.InsertCoin(Coin('Dollars'))
Coke.Select(1)
Coke.Deliver()
