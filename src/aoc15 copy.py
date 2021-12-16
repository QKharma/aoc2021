import copy
import time
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
nodes = []
new_nodes = []
starting_value = 0
node_grid = []

for y in range(len(rows)):
  row = []
  for x in range(len(rows[0])):
    row.append(Node(x,y,None,0))
  node_grid.append(row)

node_grid[0][0].value = 0
node_grid[0][0].discovered = True

new_nodes.append(Node(0,0,None,0))

while end_reached is False:

  min_node = Node(0,0,None,sys.maxsize)
  for row in node_grid:
    for node in row:
      if node.passed is False and node.discovered is True:
        if node.value < min_node.value:
          min_node = node

  print(min_node.x,min_node.y)
  print(min_node.value)

  node_grid[min_node.y][min_node.x].passed = True
  adj = return_adjacent(min_node.y,min_node.x)
  for new in adj:
    print(new)
    if node_grid[new[1][0]][new[1][1]].passed is False:
    #if not [n.passed for n in new_nodes if n.x == new[1][1] and n.y == new[1][0]]:
      node_grid[new[1][0]][new[1][1]].parent = min_node
      node_grid[new[1][0]][new[1][1]].value = new[0]+min_node.value
      node_grid[new[1][0]][new[1][1]].discovered = True
      #new_nodes.append(Node(new[1][1],new[1][0],min_node,new[0]+min_node.value))

  #print(len(new_nodes))
  #print(min_node.value)

  if node_grid[9][9].value != 0:
    end_reached = True

print(node_grid[9][9].value)