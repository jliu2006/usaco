"""
ID: jackliu08
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

n = int(fin.readline().strip('\n')) + 1899
days = 0

count_13 = [0, 0, 0, 0, 0, 0, 1]

def checkLeapYear(year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0:
        months[1] = 29
    elif (year % 4 == 0) and (year % 100 != 0):
        months[1] = 29
    return months
    
year = 1900
day = 6
while year <= n:
    month = 0
    months = checkLeapYear(year)
    while month <= 10:
        day = day + months[month]
        day = day % 7
        count_13[day] += 1
        month += 1
    if year != n:
        day = day + months[month]
        day = day % 7
        count_13[day] += 1

    year += 1

out_str = str(count_13[6]) + ' '
for num in range(6):
    out_str = out_str + str(count_13[num]) + ' '

out_str = out_str[:-1]
out_str = out_str + '\n'
fout.write(out_str)
fout.close()