print("Square you Name?")

CatchTheException = input("Do You want to Square you Name? -Y for Yes ")

if not (CatchTheException.upper() == "Y"):
     Xception = 3 / 0
try:
     Xception = 3 / 0
except ZeroDivisionError as e:
     print("You squared you name:", e)

print("Exceptional Run is finished")
