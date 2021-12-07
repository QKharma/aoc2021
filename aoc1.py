input_file = open('./inputs/aoc1.txt', 'r')
input = input_file.read().split('\n')
input = [int(x) for x in input]

previous_sum = 0
increases = 0

for i in range(0, len(input) - 1):

    sum = (input[i - 1] + input[i] + input[i + 1])

    if sum > previous_sum:
        increases += 1

    previous_sum = sum

print(increases - 1)
