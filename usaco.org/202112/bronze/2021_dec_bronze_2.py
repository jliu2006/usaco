# problem 2: air cownditioning

n = int(input())
final_temp = input()
final_temp = final_temp.split(' ')
final_temp = [int(i) for i in final_temp]

init_temp = input()
init_temp = init_temp.split(' ')
init_temp = [int(i) for i in init_temp]
mods = 0
i = 0

def getLastIndex(init_temp, final_temp, change):
    i = len(init_temp)-1
    while i >= 0:
        delta = final_temp[i] - init_temp[i]
        if (delta > 0) and (change == 'add'):
            return i
        elif (delta < 0) and (change == 'minus'):
            return i
        i -= 1

def tempChange(init_temp, final_temp, change, start, end, mods):
    while final_temp[start] - init_temp[start] != 0:
        for i in range(start, end+1):
            if change == 'add':
                init_temp[i] = init_temp[i] + 1
            if change == 'minus':
                init_temp[i] = init_temp[i] - 1
        mods += 1
    return init_temp, mods
    
for i in range(n):
    delta = final_temp[i] - init_temp[i]
    if delta == 0:
        continue
    elif delta > 0:
        change = 'add'
    elif delta < 0:
        change = 'minus'
    last_index = getLastIndex(init_temp, final_temp, change)
    init_temp, mods = tempChange(init_temp, final_temp, change, i, last_index, mods)
    change = ''

print('modifications:', mods)