# problem 1: year of the cow
# find the number of years apart Bessie and Elsie are

# ex. Mildred born in previous Dragon year from Bessie
    # important words are 0, 3, 4, 7
    # Mildred previous Dragon Bessie

import sys

def readTestCases(filename):
    cow_info = []
    f = open(filename, "r")
    n_str = f.readline() # read first line as number of test cases
    n = int(n_str)
    for i in range(n):
        cow = f.readline()
        cow = cow.strip('\n')
        cow = cow.split(' ')
        line = [cow[0], cow[3], cow[4], cow[7]]
        cow_info.append(line)
    return cow_info

cow_info = readTestCases('data.in')
print(cow_info)
# work backwards from Bessie

def getCowDiff(cow1_year, cow2_year, compare): # ex. 'Dragon' (Mildred), 'Ox' (Bessie), 'previous'
    zodiac = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
             'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']

    for idx, animal in enumerate(zodiac):
        if cow1_year == animal:
            cow1_year = idx
        if cow2_year == animal:
            cow2_year = idx
    
    diff = cow1_year - cow2_year

    if compare == 'previous':
        if diff == 0:
            diff = -12
        else:
            diff = diff - 12
        return diff
    elif compare == 'next':
        if diff == 0:
            diff = 12
        elif diff < 0:
            diff = diff + 12
        return diff

def findComparePath(cow_list): # work from Elsie to Bessie, finds order of cows to compare
    cow_order = ['Elsie']
    curr_cow = 'Elsie'
    curr_line = 0
    while curr_cow != 'Bessie':
        line = cow_list[curr_line]
        if line[0] == curr_cow:
            curr_cow = line[3]
            cow_order.insert(0, curr_cow)
        curr_line += 1
        if curr_line == len(cow_list):
            curr_line = 0
    
    return cow_order

order = findComparePath(cow_info)
#print('ORDER:', order)
cow2_year = 'Ox'
diff_list = []
for i in range(len(order)):
    if i == len(order)-1:
        break
    for line in cow_info:
        if (line[3] == order[i]) and (line[0] == order[i+1]):
            #print(line)
            cow1 = line[0]
            cow1_year = line[2]
            cow2 = line[3]
            compare = line[1]

            diff = getCowDiff(cow1_year, cow2_year, compare)
            diff_list.append(diff)
            #print(cow1_year, diff, compare, cow2_year)
            cow2_year = cow1_year

final_diff = abs(sum(diff_list))

fout = open('data.out', 'w')
fout.write(str(final_diff))