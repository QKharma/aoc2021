input_file = open('./inputs/aoc7.txt', 'r')
input = input_file.read().split(',')
input = [int(x) for x in input]
input.sort()

print(input)

def calc_fuel(distance):
    return distance*(distance+1)/2

fuel_min = 99999999999
fuel = 0

for i in range(0,input[-1]):
    print(i)
    fuel = 0
    for crab in input:
        fuel += calc_fuel(abs(crab-i))
    if fuel < fuel_min:
        fuel_min = fuel

print(int(fuel_min))