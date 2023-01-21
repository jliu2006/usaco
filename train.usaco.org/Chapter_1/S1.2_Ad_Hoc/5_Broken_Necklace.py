"""
ID: jackliu08
LANG: PYTHON3
TASK: beads
"""

def checkCorner(beads):
    length = len(set(beads))
    if length == 1:
        return True
    elif (length == 2) and ('w' in set(beads)):
        return True
    return False

def findColorWhiteFront(beads):
    idx = 0
    while idx < len(beads):
        if beads[idx] != 'w':
            return beads[idx]
        idx += 1

def readFront(beads):
    idx = 0
    if beads[idx] == 'w':
        color = findColorWhiteFront(beads)
    else:
        color = beads[idx]
    
    break_point = False
    streak = 0
    while not break_point:
        if (beads[idx] != color) and (beads[idx] != 'w'):
            break_point = True
        else:
            streak += 1
        idx += 1
    cut_beads = beads[idx-1:]
    return streak, cut_beads

def findColorWhiteBack(beads):
    idx = -1
    while idx >= -len(beads):
        if beads[idx] != 'w':
            return beads[idx]
        idx -= 1

def readBack(beads):
    length = len(set(beads))
    if checkCorner(beads):
        return len(beads)
    else:
        idx = -1
        if beads[idx] == 'w':
            color = findColorWhiteBack(beads)
        else:
            color = beads[idx]
        break_point = False
        streak = 0
        while not break_point:
            if (beads[idx] != color) and (beads[idx] != 'w'):
                break_point = True
            else:
                streak += 1
            idx -= 1
        return streak


fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

n = int(fin.readline().strip('\n'))
beads = list(fin.readline().strip('\n'))

def main(beads):
    idx = 0
    streak = 0
    while idx < n:
        split = beads[idx:] + beads[:idx]
        front, cut_beads = readFront(split)
        back = readBack(cut_beads)
        streak = max(streak, front + back)
        idx += 1

    return streak

if checkCorner(beads):
    streak = n
else:
    streak = main(beads)
    
out = str(streak) + '\n'
fout.write(out)
fout.close()