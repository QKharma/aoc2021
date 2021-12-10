import math

input_file = open('./inputs/aoc10.txt', 'r')
rows = input_file.read().split('\n')

points = {
    ')': 3,
    '}': 1197,
    ']': 57,
    '>': 25137
}

points2 = {
    '(': 1,
    '{': 3,
    '[': 2,
    '<': 4
}

res = 0
i = 0

incomplete = []

for row in rows:
    i += 1
    chunks = []
    wrong = []
    for char in row:
        if char in ['(','{','[','<']:
            chunks.append(char)
        if char in [')','}',']','>']:
            if char == ')':
                if chunks[-1] == '(':
                    chunks.pop()
                else:
                    wrong.append(char)
            if char == '}':
                if chunks[-1] == '{':
                    chunks.pop()
                else:
                    wrong.append(char)
            if char == ']':
                if chunks[-1] == '[':
                    chunks.pop()
                else:
                    wrong.append(char)
            if char == '>':
                if chunks[-1] == '<':
                    chunks.pop()
                else:
                    wrong.append(char)

    if wrong != []:
        res += points[wrong[0]]
    else:
       incomplete.append(chunks)

print('part 1: ', res)

results = []

for elem in incomplete:
    res = 0
    elem = elem[::-1]
    for char in elem:
        res = res*5
        res += points2[char]
    results.append(res)
results.sort()

print('part 2: ', results[math.floor((len(results)/2))])