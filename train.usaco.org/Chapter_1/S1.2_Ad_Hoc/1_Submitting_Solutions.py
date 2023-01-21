"""
ID: Jiahe Liu [jackliu8]
TASK: test
LANG: PYTHON3
"""
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
x, y = map(int, fin.readline().split())
sum = x + y
fout.write (str(sum) + '\n')
fout.close()