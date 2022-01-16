import math
from ast import literal_eval

input_file = open('./inputs/aoc18.txt', 'r')
rows = input_file.read().split('\n')

class Node:
  def __init__(self, input, depth):
    self.left = None
    self.right = None
    self.data = input
    self.depth = depth
    self.ref_id = None

    if type(self.data) is not int:
      depth += 1
      node_left = Node(self.data[0], depth)
      node_right = Node(self.data[1], depth)
      self.left = node_left
      self.right = node_right

  def list_value_references(self, ref_arr):
    if self.left:
      self.left.list_value_references(ref_arr)
    if self.right:
      self.right.list_value_references(ref_arr)
    if not (self.left and self.right):
      ref_arr.append(self)
      self.ref_id = len(ref_arr)-1

  def update_tree(self):
    if (self.left and self.right):
      self.left.update_tree()
      self.right.update_tree()
      self.data = [self.left.data, self.right.data]
  
  def explode(self, references):
    if (self.left and self.right):
      if self.depth == 4:
        ref_id_left = self.left.ref_id
        ref_id_right = self.right.ref_id
        if not ref_id_left == 0:
          references[ref_id_left-1].data += self.left.data
        if not ref_id_right > len(references)-2:
          references[ref_id_right+1].data += self.right.data
        self.left = None
        self.right = None
        self.data = 0
        return True
      else:
        exploded = self.left.explode(references)
        if not exploded:
          exploded = self.right.explode(references)
        return exploded

  def split(self):
    if not (self.left and self.right):
      if self.data > 9:
        self.left = Node(math.floor(self.data/2),self.depth+1)
        self.right = Node(math.ceil(self.data/2),self.depth+1)
        return True
    else:
      split = self.left.split()
      if not split:
        split = self.right.split()
      return split

  def magnitude(self):
    if (self.left and self.right):
      left = self.left.magnitude()
      right = self.right.magnitude()
      return left*3 + right*2
    else:
      return self.data

root = Node(literal_eval(rows[0]),0)

for row in range(1,len(rows)):
  root = Node([root.data,literal_eval(rows[row])],0)
  while True:
    references = []
    root.list_value_references(references)

    #explode
    exploded = root.explode(references)
    root.update_tree()
    if exploded:
      continue

    #otherwise split
    split = root.split()
    root.update_tree()
    if split:
      continue
    break

print(root.data)
print(root.magnitude())