"""
ID: jackliu08
LANG: PYTHON3
TASK: milk
"""

fin = open('milk.in', 'r')
fout = open('milk.out', 'w')

nums = fin.readline().strip('\n')
nums = [int(i) for i in nums.split(' ')]
quota = nums[0]
farmers = nums[1]

def getCost(quota, produ):
    cost = 0
    while quota > 0:
        for line in produ:
            if line[1] <= quota:
                quota -= line[1]
                cost += line[0]*line[1]
            else:
                cost += line[0]*quota
                quota = 0
    return cost


produ = []
for i in range(farmers):
    line = fin.readline().strip('\n')
    line = [int(i) for i in line.split(' ')]
    produ.append(line)

produ.sort()
cost = getCost(quota, produ)

out = str(cost) + '\n'
fout.write(out)
fout.close()

