"""
ID: jackliu08
LANG: PYTHON3
TASK: namenum
"""

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')

fnames = open('dict.txt', 'r+')
names = fnames.read().strip('\n')
names = names.split()
fnames.close()

letters_dict = {2: ['A', 'B', 'C'], 
                3: ['D', 'E', 'F'], 
                4: ['G', 'H', 'I'], 
                5: ['J', 'K', 'L'], 
                6: ['M', 'N', 'O'], 
                7: ['P', 'R', 'S'], 
                8: ['T', 'U', 'V'], 
                9: ['W', 'X', 'Y']}

def checkValid(nums, names, letters):
    idx = 0
    good_lets = []
    valid_names = []
    while idx < len(nums):
        number = nums[idx]
        good_lets.append(letters[number])
        idx += 1
    for name in names:
        good = True
        for i in range(len(good_lets)):
            if name[i] not in good_lets[i]:
                good = False
        if good:
            valid_names.append(name)
    return valid_names
        

nums = fin.readline().strip('\n')
nums = [int(i) for i in list(nums)]

valid = []

for name in names:
    if len(name) == len(nums):
        valid.append(name)

good_names = checkValid(nums, valid, letters_dict)

if len(good_names) == 0:
    fout.write('NONE\n')
else:
    for name in good_names:
        fout.write(name + '\n')
fout.close