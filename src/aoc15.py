import copy
import time

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

new_nodes.append(Node(0,0,None,0))

while end_reached is False:

  min_node = Node(0,0,None,1000000000000000000000000000000000)
  for node in new_nodes:
    if node.passed is False:
      if node.value < min_node.value:
        min_node = node

  min_node.passed = True
  adj = return_adjacent(min_node.y,min_node.x)
  for new in adj:
    if not [n.passed for n in new_nodes if n.x == new[1][1] and n.y == new[1][0]]:
      new_nodes.append(Node(new[1][1],new[1][0],min_node,new[0]+min_node.value))

  if (9,9) in [(n.x,n.y) for n in new_nodes]:
    end_reached = True

print([n.value for n in new_nodes if (n.x,n.y) == (9,9)])