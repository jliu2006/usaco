# problem 1: cow college
# dec 17 2022 by jiahe liu
    
n = int(input())
line = input().split(' ')
line = [int(i) for i in line]

line.sort()
rich = max(line)
poor = min(line)

money = 0
final_tuition = 0

for idx in range(len(line)):
    
    payers = len(line) - idx
    tuition = line[idx]

    if payers*tuition > money:
        final_tuition = tuition
        money = payers*tuition

print(int(money), int(final_tuition))




