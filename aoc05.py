input_file = open('./inputs/aoc5.txt', 'r')
line_inputs = input_file.read().split('\n')

class Line():

  def __init__(self, line_input):
    origin = line_input.split(' -> ')[0]
    destination = line_input.split(' -> ')[1]

    self.line = line_input

    self.x1 = int(origin.split(',')[0])
    self.y1 = int(origin.split(',')[1])
    self.x2 = int(destination.split(',')[0])
    self.y2 = int(destination.split(',')[1])

    if self.x1 == self.x2 or self.y1 == self.y2:
      self.diagonal = False
    else:
      self.diagonal = True

  def calc_positions_1(self):

    positions = []

    if self.diagonal is False:
      if self.x1 == self.x2:
        if self.y1 < self.y2:
          for i in range(self.y1, self.y2+1, 1):
            positions.append([self.x1,i])
          return positions
        else:
          for i in range(self.y2, self.y1+1, 1):
            positions.append([self.x1,i])
          return positions
      elif self.y1 == self.y2:
        if self.x1 < self.x2:
          for i in range(self.x1, self.x2+1, 1):
            positions.append([i,self.y1])
          return positions
        else:
          for i in range(self.x2, self.x1+1, 1):
            positions.append([i,self.y1])
          return positions
    else:
      return []

  def calc_positions_2(self):

    positions = []

    if self.diagonal is False:
      if self.x1 == self.x2:
        if self.y1 < self.y2:
          for i in range(self.y1, self.y2+1, 1):
            positions.append([self.x1,i])
          return positions
        else:
          for i in range(self.y2, self.y1+1, 1):
            positions.append([self.x1,i])
          return positions
      elif self.y1 == self.y2:
        if self.x1 < self.x2:
          for i in range(self.x1, self.x2+1, 1):
            positions.append([i,self.y1])
          return positions
        else:
          for i in range(self.x2, self.x1+1, 1):
            positions.append([i,self.y1])
          return positions
    else:
      i = self.x1
      o = self.y1
      if self.x1 < self.x2 and self.y1 < self.y2:
        for _ in range(self.x1, self.x2+1, 1):
            positions.append([i,o])
            i += 1
            o += 1
        return positions
      elif self.x1 > self.x2 and self.y1 < self.y2:
        for _ in range(self.x2, self.x1+1, 1):
            positions.append([i,o])
            i -= 1
            o += 1
        return positions
      elif self.x1 > self.x2 and self.y1 > self.y2:
        for _ in range(self.x2, self.x1+1, 1):
            positions.append([i,o])
            i -= 1
            o -= 1
        return positions
      elif self.x1 < self.x2 and self.y1 > self.y2:
        for _ in range(self.x1, self.x2+1, 1):
            positions.append([i,o])
            i += 1
            o -= 1
        return positions

lines = []

for input in line_inputs:
    lines.append(Line(input))

positions = []

for line in lines:
  positions.append(line.calc_positions_2())

position_count = {}

for position_set in positions:
  if position_set == []:
    pass
  else:
    for position in position_set:
      try:
        position_count[str(position)] += 1
      except KeyError:
        position_count[str(position)] = 1

overlapping_count = 0

for key, value in position_count.items():
  if value > 1:
    overlapping_count += 1

print(overlapping_count)