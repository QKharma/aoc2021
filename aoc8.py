input_file = open('./inputs/aoc8.txt', 'r')
four_digit_displays = input_file.read().split('\n')

f_displays = []

for display in four_digit_displays:
    f_display = [display.split('|')[0].strip().split(' '),display.split('|')[1].strip().split(' ')]
    f_displays.append(f_display)
i = 0
results = []
for display in f_displays:
    n_1 = None
    n_2 = None
    n_3 = None
    n_4 = None
    n_5 = None
    n_6 = None
    n_7 = None
    n_8 = None
    n_9 = None
    n_0 = None

    bb = None

    i += 1

    for digit in display[0]:
        digit = ''.join(sorted(digit))
        if len(digit) == 2:
            n_1 = digit
        if len(digit) == 4:
            n_4 = digit
        if len(digit) == 3:
            n_7 = digit
        if len(digit) == 7:
            n_8 = digit

    for digit in display[0]:
        digit = ''.join(sorted(digit))
        if len(set(n_7).symmetric_difference(set(digit))) == 2:
            n_3 = digit
    
    bb = set(n_3).difference(set.union(set(n_4),set(n_7)))
    
    n_9 = ''.join(sorted(list(set.union(set.union(set(n_4), set(n_7)),set(bb)))))

    temp = set(n_9).difference(set(bb))

    n_0 = ''.join(sorted(set.union(set.union(set(n_8).symmetric_difference(temp),set(n_4).difference(set(n_3))),set(n_7))))
    
    for digit in display[0]:
        digit = ''.join(sorted(digit))
        if len(digit) == 6 and digit != n_9 and digit != n_0:
            n_6 = digit

    bl = set(n_6).intersection(set(n_1))
    tl = set(n_1).difference(set(bl))

    #print(set(n_9).difference(n_1))
    #print(tl)
    #print(bl)
    #print(bb)

    n_5 = ''.join(sorted(set.union(set.union(set(n_9).difference(n_1),set(bl)),set(bb))))

    br = set(n_8).difference(set.union(set(n_5),set(n_1)))

    n_2 = ''.join(sorted(set.union(set(n_3).difference(set(bl)),set(br))))

    #tt = set(n_1).symmetric_difference(set(n_7))
    #print(i, ': ', tt, bb)
    print(i, ': ', n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8,n_9,n_0)

    result_num_str = ''

    for digit in display[1]:
        digit = ''.join(sorted(digit))

        if digit == n_1:
            result_num_str += '1'
        if digit == n_2:
            result_num_str += '2'
        if digit == n_3:
            result_num_str += '3' 
        if digit == n_4:
            result_num_str += '4'
        if digit == n_5:
            result_num_str += '5'
        if digit == n_6:
            result_num_str += '6'
        if digit == n_7:
            result_num_str += '7'
        if digit == n_8:
            result_num_str += '8'
        if digit == n_9:
            result_num_str += '9'
        if digit == n_0:
            result_num_str += '0'
    
    print(i, ': ', result_num_str)

    results.append(int(result_num_str))

result = 0
for res in results:
    result += res

print(result)
'''
count = 0
for output in outputs:
    if len(output) == 2:
        count += 1
    if len(output) == 4:
        count += 1
    if len(output) == 3:
        count += 1
    if len(output) == 7:
        count += 1

print(count)
'''
