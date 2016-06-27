print("As of 2014, the highest transistor count in a "
      "commercially available CPU is over 4.3 billion "
      "transistors, in Intel's 15-core Xeon IvyBridge-EX.") 

po = 4300000000

year1 = int(input("This Year: "))

year2 = int(input("Future Year: "))

yeartotal = year2 - year1

n = float(yeartotal / 2) # 18 months

pn = po * (2 ** n)

print("This total number of transistors are: ", pn)
