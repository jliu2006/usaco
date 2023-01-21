# problem 3: reverse engineering
# dec 17 2022 by jiahe liu

def reverseEngineerCase(n, m, arr_in, arr_out):
    idx = 0
    line = 0
    working = []
    while idx < n:
        check = False
        zero_to_zero = False
        zero_to_one = False
        one_to_zero = False
        one_to_one = False

        for line in range(m):
            if line in working:
                continue

            elif check == False:
                if (arr_in[line][idx] == 0) and (arr_out[line] == 0):
                    zero_to_zero = True
                elif (arr_in[line][idx] == 0) and (arr_out[line] == 1):
                    zero_to_one = True
                elif (arr_in[line][idx] == 1) and (arr_out[line] == 0):
                    one_to_zero = True
                else:
                    one_to_one = True
                check = True
        
            elif zero_to_zero == True:
                if (arr_in[line][idx] == 0) and (arr_out[line] == 0):
                    working.append(line)
                    continue
                elif (arr_in[line][idx] == 1) and (arr_out[line] == 1):
                    working.append(line)
                    continue
            elif zero_to_one == True:
                if (arr_in[line][idx] == 0) and (arr_out[line] == 1):
                    working.append(line)
                    continue
                elif (arr_in[line][idx] == 1) and (arr_out[line] == 0):
                    working.append(line)
                    continue
            elif one_to_zero == True:
                if (arr_in[line][idx] == 1) and (arr_out[line] == 0):
                    working.append(line)
                    continue
                elif (arr_in[line][idx] == 0) and (arr_out[line] == 1):
                    working.append(line)
                    continue
            elif one_to_one == True:
                if (arr_in[line][idx] == 1) and (arr_out[line] == 1):
                    working.append(line)
                    continue
                elif (arr_in[line][idx] == 0) and (arr_out[line] == 0):
                    working.append(line)
                    continue
        idx += 1
    if len(working) == len(arr_out):
        return "OK"
    return "LIE"

T = int(input())
i = 0
res = []
while i < T:
    newline = input()
    nm = list(input().split(' '))
    nm = [int(i) for i in nm]
    n = nm[0]
    m = nm[1]

    arr_in = []
    arr_out = []
    for j in range(m):

        line = input().split(' ')
        inp = list(line[0])
        inp = [int(k) for k in inp]
        arr_in.append(inp)
        out = int(line[1])
        arr_out.append(out)

    res.append(reverseEngineerCase(n, m, arr_in, arr_out))
    i += 1

for item in res:
    print(item)


