option1 = int(input("1)Insert your card \n2)Cancel\n"))

while ((option1 != 1) & (option1 != 2)):
    option1 = int(input("\nWrong option!\n\n1)Insert your card \n2)Cancel\n"))

if option1 == 1:
    option2 = 0
    ok1 = ' '
    ok2 = ' '
    ok3 = ' '
    ok4 = ' '
    while option2 != 5:
        option2 = int(input("You are identified. Please select action:\n"
                            "1) Clean your bedroom\n"
                            "2) Clean your living room\n"
                            "3) Clean your restroom\n"
                            "4) Clean your Kitchen\n"
                            "5) Cancel\n"))
        if option2 == 1:
            print("We have clean your bedroom.")
            ok1 = 'bedroom'
        elif option2 == 2:
            print("We have clean your living room.")
            ok2 = 'living room'
        elif option2 == 3:
            print("We have clean your restroom.")
            ok3 = 'restroom'
        elif option2 == 4:
            print("We have clean your kitchen.")
            ok4 = 'kitchen'
        elif option2 == 5:
            print("We have cleanned your: ", ok1,',' ,ok2,',' ,ok3,',' ,ok4 ,"\nLeave")
        else:
            print("Wrong option")

