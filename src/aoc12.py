input_file = open('./inputs/aoc12.txt', 'r')
rows = input_file.read().split('\n')

class Cave():
  def __init__(self, name):
    self.name = name
    self.connections = []

  def add_connection(self, cave):
    self.connections.append(cave)

class Results():
  def __init__(self):
    self.results = []

caves = []
cave_names = []

for row in rows:
  for cave_name in row.split('-'):
    if cave_name in cave_names:
      pass
    else:
      caves.append(Cave(cave_name))
      cave_names.append(cave_name)

for connection in rows:
  connection = connection.split('-')
  for cave in caves:
    if cave.name == connection[0]:
      cave.add_connection(connection[1])
    if cave.name == connection[1]:
      cave.add_connection(connection[0])

print([(x.name, x.connections) for x in caves])
print([x.connections for x in caves if x.name == 'start'][0])

def get_connections(caves,start,paths,res,iter=0):

  if iter == 0:
    for c in [x.connections for x in caves if x.name == start][0]:
      paths.append([start,c])
      iter += 1

    get_connections(caves,start,paths,res,iter)
    return

  if iter == 20:
    return

  iter += 1

  for p in paths:
    if 'end' in p and p not in res.results:
      res.results.append(p)

  if iter > 1:
    for p in paths:
      last_c = p[-1]
      new_paths = []
      has_duplicate = False
      if last_c == 'end' or last_c == 'start':
        continue
      for c in [x.connections for x in caves if x.name == last_c][0]:
        for c_d in p:
          if p.count(c_d) > 1 and c_d != c_d.upper():
            has_duplicate = True

        if c in p and c != c.upper() and has_duplicate is True:
          continue
        
        new_p = []
        for c_t in p:
          new_p.append(c_t)
        new_p.append(c)
        new_paths.append(new_p)

      get_connections(caves,start,new_paths,res,iter)

res  = Results()

get_connections(caves,'start',[],res)

print(res.results)
print(len(res.results))
