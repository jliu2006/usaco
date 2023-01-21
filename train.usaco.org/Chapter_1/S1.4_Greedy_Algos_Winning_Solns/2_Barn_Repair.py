"""
ID: jackliu08
LANG: PYTHON3
TASK: barn1
"""

fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')

nums = fin.readline().strip('\n')
nums = [int(i) for i in nums.split(' ')]
boards = nums[0]
stalls = nums[1]
occupied = nums[2]

def calcBoards(boards, arr, num):
    diffs = []
    arr.sort()
    num -= num-arr[-1]
    num -= arr[0]-1

    for i in range(len(arr)-1):
        diffs.append(arr[i+1]-arr[i]-1)
    diffs.sort()
    for j in range(1, min(len(arr), boards)):
        num -= diffs[-j]

    return num

arr = []
for i in range(occupied):
    index = int(fin.readline().strip('\n'))
    arr.append(index)

if boards >= occupied:
    num = occupied
else:
    num = calcBoards(boards, arr, stalls)

out = str(num)+'\n'
fout.write(out)
fout.close()
