import sys

input_file = open('./inputs/aoc15.txt', 'r')
rows = input_file.read().split('\n')

class Node():
  def __init__(self,x,y,parent,value):
    self.coords = (int(x),int(y))
    self.x = int(x)
    self.y = int(y)
    self.parent = parent
    self.value = value
    self.passed = False
    self.discovered = False
    
def return_adjacent(y,x):
    nodes = []
    if y != 0:
        nodes.append((int(rows[y-1][x]),(y-1,x)))
    if x != 0:
        nodes.append((int(rows[y][x-1]),(y,x-1)))
    try:
        nodes.append((int(rows[y+1][x]),(y+1,x)))
    except:
        pass
    try:
        nodes.append((int(rows[y][x+1]),(y,x+1)))
    except:
        pass
    
    return nodes

end_reached = False
node_grid = []
grid_size = len(rows)

for y in range(len(rows)):
  row = []
  for x in range(len(rows[0])):
    row.append(Node(x,y,None,0))
  node_grid.append(row)

node_grid[0][0].value = 0
node_grid[0][0].discovered = True

while end_reached is False:

  min_node = Node(0,0,None,sys.maxsize)
  for row in node_grid:
    for node in row:
      if node.passed is False and node.discovered is True:
        if node.value < min_node.value:
          min_node = node

  node_grid[min_node.y][min_node.x].passed = True
  adj = return_adjacent(min_node.y,min_node.x)
  for new in adj:
    if node_grid[new[1][0]][new[1][1]].passed is False and node_grid[new[1][0]][new[1][1]].discovered is False:
      node_grid[new[1][0]][new[1][1]].parent = min_node
      node_grid[new[1][0]][new[1][1]].value = new[0]+min_node.value
      node_grid[new[1][0]][new[1][1]].discovered = True

  if node_grid[grid_size-1][grid_size-1].value != 0:
    end_reached = True

print(node_grid[grid_size-1][grid_size-1].value)