input_file = open('./inputs/aoc6.txt', 'r')
input = input_file.read().split(',')

fishes = []

for elem in input:
    fishes.append(int(elem))

age_groups = [0,0,0,0,0,0,0,0,0]
to_add = [0,0,0,0,0,0,0,0,0]

for fish in fishes:
    age_groups[fish] += 1

for i in range(0,256):
    print(i, ' : ', age_groups)
    for i in range(0,len(age_groups)):
        if i == 6:
            to_add[i] = age_groups[i+1] + age_groups[0]
        elif i == 8:
            to_add[i] = age_groups[0]
        else:
            to_add[i] = age_groups[i+1]

    for i in range(0,len(age_groups)):
        age_groups[i] = to_add[i]

print(sum(age_groups))
