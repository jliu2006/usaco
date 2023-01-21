"""
ID: jackliu08
LANG: PYTHON3
TASK: dualpal
"""

fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

nums = fin.readline().strip('\n')
nums = nums.split(' ')
nums = [int(i) for i in nums]
palins = nums[0]
start = nums[1]

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

def checkPalindrome(number):
    check = list(number)
    return True if check[::-1] == check else False

n = 0
num = start+1
while n < palins:
    checks = 0
    for b in range(2, 11):
        n_base = convertBase(num, b)
        if checkPalindrome(n_base):
            checks += 1

    if checks >= 2:
        n += 1
        n_final = ''.join([str(i) for i in n_base])
        out = n_final + '\n'
        fout.write(out)
    num += 1

fout.close()
