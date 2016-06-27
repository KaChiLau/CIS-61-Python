"""OUTPUT
>>> ================================ RESTART ================================
>>> 
please enter a principal: $1000
Please enter an interest rate: %10
Please enter amount of years: 2
The balance is :  1210.0000000000002
>>> 
"""

principal = int(input("please enter a principal: $"))

interest = int(input("Please enter an interest rate: %"))

years = int(input("Please enter amount of years: "))

balance = principal * ((1 + (interest/100)) ** years)

print("The balance is : ", balance)


