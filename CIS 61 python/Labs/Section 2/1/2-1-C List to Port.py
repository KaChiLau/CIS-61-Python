MyList = ["Oakland", "Long Beach", "Hong Kong", "kaohsiung", "Naha", "Yokohama", "Oakland"]

print("[ 1 ]Oakland\n[ 2 ]LongBeach\n[ 3 ]HongKong\n[ 4 ]Kaohsiung\n[ 5 ]Naha\n[ 6 ]Yokohama\n[ 7 ]Oakland")

port = int(input("Please select the port you want to correct: "))

i = 0
while(i < 7):
    if port - 1 == i:
        newport = str(input("Please enter the new port: "))
        MyList[i] = newport
    i += 1

i = 0
while i < 7:
    print('[', i + 1, ']', MyList[i])
    i += 1
