

for m in range(50):
    res = set()
    for i in range(m+1):
        for j in range(m+1):
            res.add(i**2+j**2)
    res = list(res)
    print(len(res))