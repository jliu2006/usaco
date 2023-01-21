# problem 1: lonely pictures

n = input()
cow_list = list(str(input()))

def findLonelyPictures(line_of_cows):
    lonely_pics = 0
    for i in range(3, len(line_of_cows)+1):
        j = 0
        while j <= len(line_of_cows)-i:
            picture = line_of_cows[j:j+i]
            print(picture)
            guernsey = sum(1 for i in picture if i == 'G')
            holstein = sum(1 for i in picture if i == 'H')
            j += 1
            if guernsey == 1 or holstein == 1:
                lonely_pics += 1
    return lonely_pics

num_lonely = findLonelyPictures(cow_list)
print(num_lonely)
        

