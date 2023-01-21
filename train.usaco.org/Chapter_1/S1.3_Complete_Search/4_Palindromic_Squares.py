"""
ID: jackliu08
LANG: PYTHON3
TASK: palsquare
"""

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

base = int(fin.readline().strip('\n'))

def convertBase(num, base):
    val = 1
    new_num = []
    while val < num:
        val = val*base
    while num > 0:
        if val <= num:
            new_digit = int(num/val)
            new_num.append(new_digit)
            num = num - val*new_digit
        elif val > num:
            new_num.append(0)
        val = int(val/base)

    while (val > 0):
        new_num.append(0)
        val = int(val/base)
    
    while new_num[0] == 0:
        new_num = new_num[1:]

    return new_num

def numToLetter(num):
    letters = {10: 'A', 11: 'B', 12: 'C',
            13: 'D', 14: 'E', 15: 'F',
            16: 'G', 17: 'H', 18: 'I',
            19: 'J', 20: 'K'}
    for i in range(len(num)):
        if num[i] in list(letters.keys()):
            num[i] = letters[num[i]]
    return num
            

def checkPalindrome(number):
    check = list(number)
    return True if check[::-1] == check else False

for n in range(1, 301):
    n_base = convertBase(n, base)
    n_base = numToLetter(n_base)
    n_final = ''.join([str(i) for i in n_base])

    square = n**2
    b_square = convertBase(square, base)
    b_square = numToLetter(b_square)
    b_square = [str(i) for i in b_square]
    if checkPalindrome(b_square):
        square_final = ''.join([i for i in b_square])
        out = n_final + ' ' + square_final + '\n'
        fout.write(out)

fout.close()

