"""
ID: jackliu08
LANG: PYTHON3
TASK: crypt1
"""

fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')

# example of a valid solution to the cryptharim
#       2 2 2
#     x   2 2
#      ------
#       4 4 4
#     4 4 4
#   ---------
#     4 8 8 4

n = int(fin.readline().strip('\n'))
nums = fin.readline().strip('\n')
nums = [str(i) for i in nums.split(' ')]

def checkMultiply(digits, all_nums):
    prod1 = int(digits[0] + digits[1] + digits[2]) * int(digits[3])
    prod2 = int(digits[0] + digits[1] + digits[2]) * int(digits[4])
    
    final = str(prod1 + prod2*10)
    #print(prod1, prod2, final)
    prod1 = str(prod1)
    prod2 = str(prod2)

    if (len(prod1) != 3) or (len(prod2) != 3) or (len(final) != 4):
        return False
    
    for i in range(3):
        j = prod1[i]
        k = prod2[i]

        if (j not in all_nums) or (k not in all_nums):
            #print("PRODUCT OUT OF LIST")
            return False
    
    for i in range(4):
        if final[i] not in all_nums:
            #print("SUM OUT OF LIST")
            return False
    
    #print("GOOD")
    return True

cases = 0

for i in range(n):
    a = nums[i]
    for j in range(n):
        b = nums[j]
        for k in range(n):
            c = nums[k]
            for l in range(n):
                d = nums[l]
                for m in range(n):
                    e = nums[m]
                    digits = [a, b, c, d, e]
                    if checkMultiply(digits, nums):
                        cases += 1

out = str(cases) + '\n'
fout.write(out)
fout.close()