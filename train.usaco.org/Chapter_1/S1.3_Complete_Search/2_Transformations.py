"""
ID: jackliu08
LANG: PYTHON3
TASK: transform
"""

fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

def getSquare(n):
    square = []
    for i in range(n):
        line = fin.readline().strip('\n')
        line = [str(i) for i in list(line)]
        square.append(line)

    return square

def checkEquality(n, sqin, sqout):
    for i in range(n):
        for j in range(n):
            if sqin[i][j] != sqout[i][j]:
                return False
    return True

def rotate90clock(n, square): # oper 1
    out = []
    reverse = square[::-1]
    for i in range(n):
        out.append([])
        for j in range(n):
            out[-1].append(reverse[j][i])
    return out

def reflectY(n, square):
    out = []
    for i in range(n):
        out.append(square[i][::-1])
    return out

def main():
    n = int(fin.readline().strip('\n'))
    sqin = getSquare(n)
    sqout = getSquare(n)

    sq_test = rotate90clock(n, sqin)
    if checkEquality(n, sq_test, sqout):
        return 1
    
    sq_test = rotate90clock(n, sq_test)
    if checkEquality(n, sq_test, sqout):
        return 2

    sq_test = rotate90clock(n, sq_test)
    if checkEquality(n, sq_test, sqout):
        return 3

    sq_test = reflectY(n, sqin)
    if checkEquality(n, sq_test, sqout):
        return 4
    
    sq_test = rotate90clock(n, sq_test)
    if checkEquality(n, sq_test, sqout):
        return 5
    
    sq_test = rotate90clock(n, sq_test)
    if checkEquality(n, sq_test, sqout):
        return 5
    
    sq_test = rotate90clock(n, sq_test)
    if checkEquality(n, sq_test, sqout):
        return 5

    if checkEquality(n, sqin, sqout):
        return 6

    return 7

transform = main()

out = str(transform) + '\n'

fout.write(out)
fout.close()
