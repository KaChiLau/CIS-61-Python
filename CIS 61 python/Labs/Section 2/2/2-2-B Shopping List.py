
list = []

k = 0
while (k != 2):
    k = int(input("Case 1)Enter an item\nCase 2)Exit(type exit to leave)\nWhich Case? "))

    if k == 1:
        c = str(input("please the name of item:"))
        list.append(c)
    elif k == 2:
        print(list)
