def number():
    ok = False
    i = 3
    while not ok:
        try:
            x = int(input("Please enter a number(1 - 10):"))
            if x >= 1 and x <= 10:
                print("Your number is in range")
                ok = True
                return ok
            else:
                print("\n\t", x, "is a invalid Value\t\n")
                i -= 1
                print("Chances left: ", i, "\n")
                ok = False

                if i == 0:
                    print("Sorry, You have used up all your chances")
                    break
        except:
            print("Invalid input")

number()
