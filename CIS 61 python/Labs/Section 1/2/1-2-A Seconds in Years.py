"""OUTPUT
>>> ================================ RESTART ================================
>>> 
please enter a whole number of years: 100
total seconds in the years:  3153600000
total pseconds in the year(including prime year):  3155760000.0
>>> 
""" 

year = int(input("please enter a whole number of years: "))

days = 365 * year

hours = days * 24

minutes = hours * 60

seconds = minutes * 60

""" seconds = year * 365 * 24 * 60 * 60 """

print("total seconds in the years: ", seconds)

prime = year / 4

pseconds = seconds + (prime * 24 * 60 * 60)

print("total pseconds in the year(including prime year): ", pseconds)
