def gradepoint():

    numberClass = int(input("Please enter the total classes you have take this semester: "))

    gradept = 0
    unit = 0
    i = 0
    for x in range(i,numberClass):

        lettergrade = str(input("Please enter the letter grade you recieved: "))
        unit = int(input("Please enter the unit: "))
        gradept = letter(lettergrade, unit) + gradept
        i += 1

    print("Total GradePoint: ", gradept)

    return gradept

def letter(lettergrade, unit):
    if lettergrade == 'A':
        letterPt = 4
    elif lettergrade == 'B':
        letterPt = 3
    elif lettergrade == 'C':
        letterPt = 2
    elif lettergrade == 'D':
        letterPt = 1
    elif lettergrade == 'F':
        letterPt = 0
    return letterPt * unit
            

def gpa():

    totalU = int(input("Please enter the total unit you have take this semester: "))

    print("Your GPAs is: ", '%.2f' % (gradepoint() / totalU))

    return


gpa()
