# problem 1: sleeping in class

def readOneTestCase(f):
    one_test_line = []
    f.readline() # read first line as number of test cases
    n_str = f.readline()
    for it in n_str.split(' '):
        one_test_line.append(it.trim('\n'))
    return one_test_line

def readTestCases():
    test_set = []
    f = open("data.in", "r")
    n_str = f.readline() # read first line as number of test cases
    n = int(n_str)
    test = []
    for i in range(0, n):
        test_set.append(readOneTestCase(f))
    return test_set

test_set = readTestCases()
# [[1, 2, 3, 1, 1, 1], [2, 2, 3], [0, 0, 0, 0, 0]]

def solve(n_list):
    print("solving...")
    print (n_list)
    modifications = 0
    maximum = max(n_list)
    while len(n_list) >= 1:  # outer loop
        i = 0
        print("cur max %d, len %d" % (maximum, len(n_list)))
        if max(n_list) == min(n_list):
            print('done')
            print(n_list)
            print(modifications)
            return modifications

        while i < len(n_list)-1:
            if n_list[i] + n_list[i+1] <= maximum:
                print("yes sum %d" %i)
                n_list[i] = n_list[i] + n_list[i+1]
                modifications += 1
                print("mods plus one %d" %modifications)
                del n_list[i+1]
                print("list len %d" %len(n_list))
            else:
                print("no sum %d" %i)
                i += 1
        maximum += 1

for it in test_set:
    mods = []
    mods.append(solve(it))