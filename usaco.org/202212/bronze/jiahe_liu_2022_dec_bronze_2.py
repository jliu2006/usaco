# problem 2: feeding the cows
# dec 17 2022 by jiahe liu

T = int(input())
res = []

def leftToRight(cows, n, K):
    patches = ['.']*n
    i = 0
    for i in range(n):
        if cows[i] in ('G', 'H'):
            patch = min(n-1, i+K)
            while (patches[patch] != cows[i]) and (patches[patch] != '.'):
                patch -= 1
            patches[patch] = cows[i]
            right = min(n, patch+K+1)
            for j in range(i, right):
                if cows[j] == patches[patch]:
                    cows[j] = '.'
            
    return(patches)

for i in range(T):
    nK = input().split(' ')
    nK = [int(i) for i in nK]
    n = nK[0]
    K = nK[1]

    cows = list(input())
    cows_left = leftToRight(cows, n, K)
    out = ''.join(cows_left)
    num = out.count('G') + out.count('H')
    print(num)
    print(out)


