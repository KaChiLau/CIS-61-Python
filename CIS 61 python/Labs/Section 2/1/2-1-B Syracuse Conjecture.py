def Hailstonesequence(n):

    print("Number: ", n)
    
    i = 1
    while (n != 1):
        if(n < 0):
            n = -n
        if(n % 2) == 0:
            n /= 2
        else:
            n *= 3
            n += 1

        i += 1

    print("Total steps: ", i)
    
    return 


j = int(input("case 1 or 2: "))

if j == 1:
    Hailstonesequence(27)
elif j == 2:
    k = int(input("please enter any number you want to test: "))
    i = 1
    while i <= k:
        Hailstonesequence(i)
        i += 1
    print("Yes, This is ONENESS")
else:
    print("Please enter 1 or 2")
