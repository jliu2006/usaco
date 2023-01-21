# problem 3: drought

array = []

n = int(input())

for i in range(0, n):
    cases = input()
    lines = input()
    lines = lines.split(' ')
    lines = [int(i) for i in lines]
    array.append(lines)

mod_array = []

def checkLine(line):
    first = line[0]
    for elem in line:
        if elem != first:
            return False
    return True

def checkNegative(line):
    for elem in line:
        if elem < 0:
            return True
    return False

def feedLine(line):
    min_hunger = min(line)
    bags_fed = 0
    while checkLine(line) != True:
        i = 0
        while i < len(line) - 1:
            if line[i] > min_hunger:
                line[i] = line[i] - 1
                line[i+1] = line[i+1] - 1
                bags_fed += 2
            else:
                min_hunger = min(line)
                i += 1
        if checkNegative(line) == True:
            return -1
    return bags_fed
    
def checkEqual(two_elems):
    if two_elems[0] == two_elems[1]:
        return 0
    else:
        return -1

for row in array:
    if len(row) > 2:
        total_bags = feedLine(row)
        mod_array.append(total_bags)
    elif len(row) == 2:
        total_bags = checkEqual(row)
        mod_array.append(total_bags)
    else:
        total_bags = 0
        mod_array.append(total_bags)

for bags in mod_array:
    print(bags)