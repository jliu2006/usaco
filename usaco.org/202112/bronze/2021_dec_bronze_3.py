# problem 3: walking home

t = int(input())

def checkStartDirections(farm):
    x = 0
    y = 0

    directions = []

    if (farm[x+1][y] == '.'):
        directions.append('down')
    if (farm[x][y+1] == '.'):
        directions.append('right')
    
    return directions
n = 3
k = 2

def clearRow(row, start, end, farm):
    for it in farm[row][start:end-start+1]:
        if it == 'H':
            return False
    return True

def clearCol(col, start, end, farm):
    for i in range(start, end+1):
        if farm[i][col] == 'H':
            return False
    return True

if direction == 'down':
    if k == 1:
        clear_col = clearCol(0, 0, n, farm)

    elif k == 2: # assume direction is 'down'
        for x in range(1, n):
            clear_col = clearCol(0, 0, x, farm)
            clear_row = (x, 0, n, farm)
            second_clear_col = clearCol(n-1, x, n, farm)
            if clear_col and clear_row and second_clear_col:
                res += 1
            
    elif k == 3:
        for x in range(1, n-2): # m is the row for first turn
            for y in range(1, n-1): # n is the row for second turn
                # check if first col from 0 to m inclusive is clear
                # check if mth row from 0 to n inclusive is clear
                clear_col = clearCol(0, 0, x, farm)
                clear_row = clearRow(y, 0, x, farm)
                second_clear_col = clearCol(x, y, n, farm)

elif direction == 'right':



def generatePaths(n, k, direction):
    turns = 0
    length = n*2
    # 0 is down, 1 is right
    # based on starting direction, generatePaths will create random arrays of length n*2
    # with k turns, being defined as the value opposite the direction
    if direction == 'down':
        



for i in range(t):
    nk = input()
    nk = nk.split(' ')
    nk = [int(i) for i in nk]

    n = nk[0]
    k = nk[1]

    farm = []

    for i in range(n):
        row = input()
        row = [*row]
        farm.append(row)
    
    directions = checkStartDirections(farm)

def recursiveCheck(k, subfarm): # get to (x, y) in one turn
    if m == 
    for m in range(len(subfarm[0])):
        for n in range(len(subfarm[0])):
            if (clearCol(0, 0, m, subfarm) and clearRow(n, 0, m, subfarm)) or (clearRow(0, 0, n, subfarm) and clearCol(m, 0, n, subfarm)):
                check_path(k-1, subfarm[m:][n:])
            