"""
ID: Jiahe Liu [jackliu8]
PROG: gift1
LANG: PYTHON3
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

def getGivers(fin):
    dict_names = {}
    n = int(fin.readline().strip('\n'))
    for i in range(n):
        name = fin.readline().strip('\n')
        dict_names[name] = [0]
    return n, dict_names

def giveMoney(d, giver, money, recievers):

    if (len(recievers) == 0) or (money == 0):
        return d

    split = money // len(recievers)
    
    leftover = money - (split*len(recievers))
    d[giver][0] -= money - leftover
    
    for person in recievers:
        d[person][0] += split
    
    return d

def readList(fin, d):
    giver = fin.readline().strip('\n')
    line = fin.readline().strip('\n').split(' ')
    line = [int(i) for i in line]

    money, num = line[0], line[1]
    recievers = []

    for i in range(num):
        name = fin.readline().strip('\n')
        recievers.append(name)
    
    d = giveMoney(d, giver, money, recievers)

    return d


n, givers = getGivers(fin)

for i in range(n):
    readList(fin, givers)

for key in givers:
    line = str(key) + ' ' + str(givers[key][0]) + '\n'
    fout.write(line)

fout.close()