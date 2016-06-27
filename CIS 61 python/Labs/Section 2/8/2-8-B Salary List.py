salaries = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

print(salaries)

def bubble(salaries):
    length = len(salaries) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if (salaries[i] < salaries[i+1]):
                sorted = False
                salaries[i], salaries[i+1] = salaries[i+1], salaries[i]

bubble(salaries)

print(salaries)

