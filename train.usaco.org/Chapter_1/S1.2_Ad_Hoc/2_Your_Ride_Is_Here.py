"""
ID: Jiahe Liu [jackliu8]
PROG: ride
LANG: PYTHON3
"""
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

def readSplitMod(fin, n):
    nums = []
    t = 0
    while t < n:
        arr = fin.readline().strip('\n')
        arr = [str(i) for i in list(arr)]
        arr_prod = 1

        for letter in arr:
            arr_prod = arr_prod * (alpha.index(letter)+1)

        mod = arr_prod % 47
        nums.append(mod)
        t += 1
    return nums

nums = readSplitMod(fin, 2)

if nums[0] == nums[1]:
    fout.write("GO\n")
else:
    fout.write("STAY\n")
fout.close()


