"""
ID: jackliu08
LANG: PYTHON3
TASK: ariprog
"""

fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')

n = int(fin.readline().strip('\n'))
m = int(fin.readline().strip('\n'))

def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x: # element is the middle
            return "yes", mid
        elif arr[mid] > x: # element is smaller than middle val
            return binarySearch(arr, low, mid - 1, x)
        else: # element is greater
            return binarySearch(arr, mid + 1, high, x)
    else: # element not in array
        return "no", None

def checkProgression(a, b, n, arr):
    i = 1
    low = 0
    while i < n:
        x = a + b*i
        work, low = binarySearch(arr, low, len(arr)-1, x)
        #print(a, b, x)
        #print(work, low)
        if work == "no":
            return False
        i += 1 
    #print("GOOD")
    return True

def getProgressions(bisquares, n): 
    bisquares = list(bisquares)
    progressions = []
    i = 0
    while i < len(bisquares):
        a = bisquares[i]
        for j in range(i+1, len(bisquares)-n+2):
            b = bisquares[j] - a
            #print(a, b)
            if (bisquares[i+n-1] > a + b * (n-1)) or bisquares[-1] < (a + b * (n-1)):
                continue
            if checkProgression(a, b, n, bisquares):
                progressions.append([a, b])
        i += 1
    return progressions

def getBisquares(m): # num bisquares increases slightly slower than m^2
    bisquares = set()
    for p in range(m+1):
        for q in range(m+1):
            ans = p**2 + q**2
            bisquares.add(ans)
    #print(bisquares)
    #print(len(bisquares))
    return bisquares

#print(n, m)
bisquares = getBisquares(m)
bisquares = list(bisquares)
bisquares.sort()
#print(bisquares)
progressions = getProgressions(bisquares, n)
progressions.sort(key = lambda x: x[1])
#print("OUT:", progressions)

if len(progressions) == 0:
    fout.write("NONE\n")
else:
    for line in progressions:
        out = str(line[0]) + ' ' + str(line[1]) + '\n'
        fout.write(out)

fout.close()