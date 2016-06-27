def total(n):
    i = 0
    temp = 0
    while i <= n:
        if (i % 2) != 0:
            temp += i
        i += 1
    return temp

print(total(39))

