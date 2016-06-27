
def normalloop(n):
    print("calling Normal loop--")
    i = 0
    while i <= n:
        print(i)
        i += 1
    return

def  recursively(n):
    i = 0
    print(n)
    if n == i:
        return 1
    return n * recursively(n - 1)

print("calling recursively--")
recursively(49)

normalloop(49)
