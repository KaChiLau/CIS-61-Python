"""
(n * (n + 1)) / 2---

# 1   triangular:  1
# 2   triangular:  3
# 3   triangular:  6
# 4   triangular:  10
# 5   triangular:  15
# 6   triangular:  21
# 7   triangular:  28
# 8   triangular:  36
# 9   triangular:  45
# 10   triangular:  55
# 11   triangular:  66
# 12   triangular:  78
# 13   triangular:  91
# 14   triangular:  105
# 15   triangular:  120
# 16   triangular:  136
# 17   triangular:  153
# 18   triangular:  171
# 19   triangular:  190
# 20   triangular:  210
# 21   triangular:  231
# 22   triangular:  253
# 23   triangular:  276
# 24   triangular:  300

( (n ** 2) + n) / 2---

# 1   triangular:  1
# 2   triangular:  3
# 3   triangular:  6
# 4   triangular:  10
# 5   triangular:  15
# 6   triangular:  21
# 7   triangular:  28
# 8   triangular:  36
# 9   triangular:  45
# 10   triangular:  55
# 11   triangular:  66
# 12   triangular:  78
# 13   triangular:  91
# 14   triangular:  105
# 15   triangular:  120
# 16   triangular:  136
# 17   triangular:  153
# 18   triangular:  171
# 19   triangular:  190
# 20   triangular:  210
# 21   triangular:  231
# 22   triangular:  253
# 23   triangular:  276
# 24   triangular:  300
"""

def triangularN1(n):

    return (n * (n + 1)) / 2

def triangularN2(n):

    return ( (n ** 2) + n) / 2

def display(n):

    print("\n(n * (n + 1)) / 2---\n")
    i = 1
    while(i < n):
        print("#", i, ' ', "triangular: ", (int)(triangularN1(i)))
        i += 1

    print("\n( (n ** 2) + n) / 2---\n")    
    i = 1
    while(i < n):
        print("#", i, ' ', "triangular: ", (int)(triangularN2(i)))
        i += 1
        
    return

n = int(input("Please enter n: "))

display(n)
