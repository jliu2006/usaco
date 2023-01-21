# problem 1: herdle
from os import remove


cow_array = []
guess_array = []
for i in range(3):
    cow_array.extend(str(input()))
for i in range(3):
    guess_array.extend(str(input()))

def getGreenYellow(answer, guess):
    green = 0
    green_array = []
    hold_ans = []
    hold_guess = []
    yellow = 0

    for i in range(len(guess)):
        if guess[i] == answer[i]:
            green += 1
            green_array.append(True)
        else:
            green_array.append(False)
    for i in range(len(guess)):
        if green_array[i] == False:
            hold_ans.append(answer[i])
            hold_guess.append(guess[i])
    for i in range(len(hold_guess)):
        for j in range(len(hold_ans)):
            if hold_guess[i] == hold_ans[j]:
                yellow += 1
                del hold_ans[j]
                break
        
    return green, yellow

greens, yellows = getGreenYellow(cow_array, guess_array)
print(greens)
print(yellows)