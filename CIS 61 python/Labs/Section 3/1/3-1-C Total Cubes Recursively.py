def sum(n):
    i = 0
    temp = 0
    while i <= n:
        if (i ** 3) >= n:
            print(i ** 3, ">", n)
            temp += (i ** 3)
        i += 1
    return temp

print(sum(13))

