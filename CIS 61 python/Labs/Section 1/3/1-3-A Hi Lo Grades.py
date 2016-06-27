"""
KaChiLau
1-3-A Hi Lo Grades
"""

test1 = int(input("please enter your grade: "))

test2 = int(input("please enter your grade: "))

test3 = int(input("please enter your grade: "))

test4 = int(input("please enter your grade: "))

test5 = int(input("please enter your grade: "))

print("Highest: ", max(test1, test2, test3, test4, test5))
print("Lowest: ", min(test1, test2, test3, test4, test5))

average = ((test1 + test2 + test3 + test4 + test5) / 5)

print("Average: ", average)


