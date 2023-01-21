"""
ID: jackliu08
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

n = int(fin.readline().strip("\n"))

arr = []

def getLongestRun(arr):
    length = 0
    pause = 0
    run_start = arr[0][0]
    run_end = arr[0][1]
    idx = 0
    while idx < len(arr):
        row = arr[idx]
        hold_start = row[0]
        hold_end = row[1] 
        if hold_start <= run_end:
            if hold_end > run_end:
                run_end = hold_end
        else:
            length = max(length, run_end - run_start)
            pause = max(pause, hold_start - run_end)
            run_start = hold_start
            run_end = hold_end
        idx += 1
    length = max(length, run_end - run_start)
    return length, pause

for i in range(n):
    times = fin.readline().strip("\n")
    times = times.split(' ')
    arr.append([int(times[0]), int(times[1])])
    arr.sort()

if n == 1:
    length = int(arr[0][1]) - int(arr[0][0])
    pause = 0
else:
    length, pause = getLongestRun(arr)

out = str(length) + ' ' + str(pause) + '\n'

fout.write(out)
fout.close()