def PrintList(TheList):
    a = 0
    while a < len(TheList):
        print("#", a,
            "is", TheList[a])
        a += 1

NamesList = [
     "C++", "Java", "Python", "C#", "COBOL",
     "FORTRAN"
]
print("Not In order-")
PrintList(NamesList)

# The SORT Routine
InOrder = False
while(not InOrder):
        InOrder = True
        n = 0
        while n < len(NamesList) - 1:
            if NamesList[n] > NamesList[n+1]:
                InOrder = False
                temp = NamesList[n]
                NamesList[n] = NamesList[n+1]
                NamesList[n+1] = temp
            n += 1

print("In order- ")
PrintList(NamesList)
