"""
class division:
    def __init__(self, num, denom):
        self.Num = num
        self.Denom = denom

    def divide(self):
        print(self.Num / self.Denom)

d = division(7,8)

d.divide()
"""

def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'You cannot divide by zero'


print("demo 7/8:", divide(7,8))

print("demo 7/0:", divide(7,0))
