input_file = open('./inputs/aoc9.txt', 'r')
rows = input_file.read().split('\n')

low_points = []

for y in range(len(rows)):
    for x in range(len(rows[0])):
        if rows[y][x] == '9':
            continue
        is_low_point = True
        if y != 0:
            try:
                if int(rows[y-1][x]) < int(rows[y][x]):
                    is_low_point = False
            except:
                pass
        if x != 0:
            try:
                if int(rows[y][x-1]) < int(rows[y][x]) :
                    is_low_point = False
            except:
                pass
        try:
            if int(rows[y+1][x]) < int(rows[y][x]) :
                is_low_point = False
        except:
            pass
        try:
            if int(rows[y][x+1]) < int(rows[y][x]) :
                is_low_point = False
        except:
            pass


        if int(rows[y][x]) == 0:
            is_low_point = True

        if is_low_point is True:
            low_points.append((y, x))

basins = []

def return_adjacent(y,x):
    y = int(y)
    x = int(x)
    points = []
    if y != 0:
        points.append((int(rows[y-1][x]),(y-1,x)))
    if x != 0:
        points.append((int(rows[y][x-1]),(y,x-1)))
    try:
        points.append((int(rows[y+1][x]),(y+1,x)))
    except:
        pass
    try:
        points.append((int(rows[y][x+1]),(y,x+1)))
    except:
        pass
    
    not_9 = []

    for point in points:
        if point[0] != 9:
            not_9.append(point)

    return not_9

def get_basin(points):

    len_p = len(points)

    new_points = set()

    for point in points:
        new_points.add(point)
        for new in return_adjacent(point[1][0],point[1][1]):
            if new[0] != 9:
                new_points.add(new)
    
    
    if len(new_points) == len_p:
        return len(points)
    else:
        return get_basin(new_points)
        
for point in low_points:
    basin = []
    y = point[0]
    x = point[1]

    point = (int(rows[y][x]), (y, x))
    basins.append(get_basin([point]))


basins.sort()
print(basins[-1]*basins[-2]*basins[-3])