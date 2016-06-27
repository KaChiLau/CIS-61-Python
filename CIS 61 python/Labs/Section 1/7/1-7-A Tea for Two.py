pour = int(input("# of pours: "))

i = 0
j = .5
while(i < pour):
    if(j < 1):
        j = j + (j /2)
        i += 1
    else:
        i = pour

print("# of pour: ", j)
