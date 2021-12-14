from collections import defaultdict

input_file = open('./inputs/aoc14.txt', 'r')
rows = input_file.read().split('\n')

template = rows[0]
rows.pop(0)
rows.pop(0)

translator = {}
for row in rows:
  match = row.split(' -> ')[0]
  new_char = row.split(' -> ')[1]
  translator[match] = ''
  translator[match] += new_char

pairs = defaultdict(int)
char_count = defaultdict(int)

for i in range(len(template)-1):
  pairs[template[i:i+2]] += 1
  char_count[template[i]] += 1

char_count[template[-1]] += 1

for step in range(40):
  new_pairs = defaultdict(int)

  for pair in pairs:

    new_pairs[pair[0]+translator[pair]] += pairs[pair]
    new_pairs[translator[pair]+pair[1]] += pairs[pair]

    char_count[translator[pair]] += pairs[pair]

  pairs = new_pairs

print(max(char_count.values())-min(char_count.values()))
