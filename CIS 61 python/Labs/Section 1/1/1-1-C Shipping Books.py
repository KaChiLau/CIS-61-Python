"""
    A Sample program to get you started
         Laney Colleg Fall 2014
      Written by KaChiLau """

"""
A website sells books and charges shipping and handling, but no tax.
The handling charge is $2.99 per book. How much would the total be for 3 books,
priced $11.66, $21.35 and $14.00?

Calculate the total in Python and paste the expression and the answer in the Notes.
"""

"""
fstbook = float(input("please input the price of the 1st book: $"))

sndbook = float(input("please input the price of the 2nd book: $"))

trdbook = float(input("please input the price of the 3rd book: $"))
"""

fstbook = 11.66

sndbook = 21.35

trdbook = 14.00

"""total = fstbook * 2.99 + sndbook * 2.99 + trdbook * 2.99"""

total = fstbook + sndbook + trdbook + (2.99 * 3)

"""
total = fstbook , 2.99 + sndbook , 2.99 ,trdbook * 2.99
print = total , total, total
"""

print("The total of 3 books is $", '%.2f' %  total)

"""
>>> ================================ RESTART ================================
>>> 
The total of 3 books is $ 55.98
>>> 
"""
