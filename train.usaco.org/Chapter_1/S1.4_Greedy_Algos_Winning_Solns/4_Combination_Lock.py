"""
ID: jackliu08
LANG: PYTHON3
TASK: combo
"""

fin = open('combo.in', 'r')
fout = open('combo.out', 'w')

def findSettings(settings, n, opener):
    for i in range(-2, 3):
        for j in range(-2, 3):
            for k in range(-2, 3):
                combo = [opener[0] + i, opener[1] + j, opener[2] + k]
                #print("BEFORE:", combo)
                for idx in range(3):
                    while combo[idx] < 1:
                        combo[idx] = (combo[idx] + n)
                    while combo[idx] > n:
                        combo[idx] = (combo[idx] - n)
                #print("AFTER:", combo)
                settings.append(combo)
    return settings


n = int(fin.readline().strip('\n'))

john = fin.readline().strip('\n')
john = [int(i) for i in john.split(' ')]

master = fin.readline().strip('\n')
master = [int(i) for i in master.split(' ')]

settings = []
settings = findSettings(settings, n, john)
settings = findSettings(settings, n, master)

settings = [tuple(i) for i in settings]
settings = set(settings)
final = len(settings)
# print(final)
out = str(final) + '\n'
fout.write(out)
fout.close