# problem 2: photoshoot

num_cows = int(input())
current_order = input()
desired_order = input()

current_array = []
for it in current_order.split(' '):
    current_array.append(it)

desired_array = []
for it in desired_order.split(' '):
    desired_array.append(it)

i = 0
modifications = 0

while i < num_cows-1:
    if desired_array[i] != current_array[i]:
        get_index = current_array.index(desired_array[i])
        current_array.insert(i, desired_array[i])
        modifications += 1
    else:
        i += 1

print(modifications)