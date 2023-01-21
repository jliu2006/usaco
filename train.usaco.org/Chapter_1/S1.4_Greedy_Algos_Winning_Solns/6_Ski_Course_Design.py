"""
ID: jackliu08
LANG: PYTHON3
TASK: skidesign
"""

fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')

n = int(fin.readline().strip('\n'))

def taxEvasion(n, hills):
    low = hills[0]
    high = hills[-1]
    final_cost = 2 ** 31 - 1
    for i in range(low, high):
        change = [0]*n
        cost = 0
        new_low = i
        new_high = i + 17
        print(new_low, new_high)
        for j in range(n):
            if hills[j] < new_low:
                change[j] = new_low - hills[j]
                #hills[j] = new_low
            elif hills[j] > new_high:
                change[j] = hills[j] - new_high
                #hills[j] = new_high
        print(change)
        for k in change:
            add = k**2
            cost += add
        final_cost = min(final_cost, cost)
    return final_cost


        

hills = []
for i in range(n):
    height = int(fin.readline().strip('\n'))
    hills.append(height)

hills.sort()
cost = taxEvasion(n, hills)

out = str(cost) + '\n'
fout.write(out)
fout.close()
