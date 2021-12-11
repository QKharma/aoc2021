import sys

input_file = open('./inputs/aoc11.txt', 'r')
rows = input_file.read().split('\n')

class Octo():

    def __init__(self, coords, energy):
        self.coords = coords
        self.x = coords[1]
        self.y = coords[0]
        self.energy = int(energy)

def define_octos():

    octos = []
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            octos.append(Octo((y,x), rows[y][x]))
    return octos

def get_adjacent(octos, s_octo):
    adjacent = []
    for octo in octos:
        if octo.coords == (s_octo.y-1, s_octo.x):
            adjacent.append(octo)
        if octo.coords == (s_octo.y-1, s_octo.x-1):
            adjacent.append(octo)
        if octo.coords == (s_octo.y, s_octo.x-1):
            adjacent.append(octo)
        if octo.coords == (s_octo.y+1, s_octo.x-1):
            adjacent.append(octo)
        if octo.coords == (s_octo.y+1, s_octo.x):
            adjacent.append(octo)
        if octo.coords == (s_octo.y+1, s_octo.x+1):
            adjacent.append(octo)
        if octo.coords == (s_octo.y, s_octo.x+1):
            adjacent.append(octo)
        if octo.coords == (s_octo.y-1, s_octo.x+1):
            adjacent.append(octo)

    return adjacent

def part1():

    octos = define_octos()

    flashes = 0

    for step in range(100):

        flashed = []
        flashed_f = []
        repeat = True

        while repeat is True:
            
            repeat = False

            for octo in octos:
                octo.energy += 1
                if octo.energy >= 10:
                    flashed.append(octo)
                    flashes += 1
                    octo.energy = -100
                    

            for f_octo in flashed:
                adj = get_adjacent(octos, f_octo)
                for octo in adj:
                    octo.energy += 1
                    if octo.energy >= 10:
                        flashed.append(octo)
                        flashes += 1
                        octo.energy = -100

            for octo in octos:
                if octo.energy >= 10:
                    repeat = True
        
        for octo in octos:
            if octo.energy < 0:
                octo.energy = 0

    print('part 1: ',flashes)

def part2():

    octos = define_octos()
    step = 0
    
    while True:
        
        step += 1
        flashed = []
        repeat = True

        while repeat is True:
            
            repeat = False

            for octo in octos:
                octo.energy += 1
                if octo.energy >= 10:
                    flashed.append(octo)
                    octo.energy = -100
                    

            for f_octo in flashed:
                adj = get_adjacent(octos, f_octo)
                for octo in adj:
                    octo.energy += 1
                    if octo.energy >= 10:
                        flashed.append(octo)
                        octo.energy = -100

            for octo in octos:
                if octo.energy >= 10:
                    repeat = True
        
        for octo in octos:
            if octo.energy < 0:
                octo.energy = 0

        if sum([x.energy for x in octos]) == 0:
            print('part 2: ',step)
            break

part1()
part2()