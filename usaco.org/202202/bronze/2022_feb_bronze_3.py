# problem 3: blocks

def permute(arr):
    res = []
    if (len(arr)) == 1:
        return [arr]
    for i in range(0, len(arr)):
        a = permute(arr[:i] + arr[i+1:])
        for it in a:
            res.append([arr[i]] + it)
    return res

def createWords(let):
    word_list = set()
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    letter_array = [let[0][a], let[1][b], let[2][c], let[3][d]]
                    permuted = permute(letter_array)
                    for lets in permuted:
                        word = lets[0] + lets[1] + lets[2] + lets[3]
                        word_list.add(word)
    return word_list

def splitWords(list):
    letter_list = []
    for word in list:
        lets = [*word]
        lets.append('')
        letter_list.append(lets)
    return letter_list

def solve():
    n = int(input())
    l = [input() for _ in range(4)]
    words_to_spell = []
    for i in range(n):
        words_to_spell.append(input())

    letters = splitWords(l)
    words = createWords(letters)

    for word in words_to_spell:
        if word in words:
            print("YES")
        else:
            print("NO")
    
    print(letters)
    print(words_to_spell)
    print(words, len(words))

solve()

