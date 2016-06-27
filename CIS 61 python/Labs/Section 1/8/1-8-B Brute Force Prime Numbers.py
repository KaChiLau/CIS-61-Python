def prime(number):

    i = 2
    while(i < 10):
        if(number % i) != 0:
            print(i, "is not a multiple of", number)
            i += 1
        else:
            return
        
    if i == 10:
        print(number, "is prime!")

    return

def Mersenne(n):

    return (2 ** n) - 1

def oddeven(number):

    if number == 2:
        print("This is an prime even number")
    else:
        if (number % 2) == 0:
            print("This is an even number")
        else:
            if(number % 3) == 0:
                print("This is an odd number")
            else:
                print("This is an prime odd number")
    return

def square(number):

    return number **(1/2)


number = int(input("Please enter a #: "))

prime(number)

oddeven(number)
