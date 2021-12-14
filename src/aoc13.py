import math

input_file = open('./inputs/aoc13.txt', 'r')
rows = input_file.read().split('\n')
folds = []

for row in rows:
  if 'fold' in row:
    folds.append(row)

for f in folds:
  rows.pop()
rows.pop()

max_y = 0
max_x = 0

for row in rows:
  x = int(row.split(',')[0])
  y = int(row.split(',')[1])
  if x > max_x:
    max_x = x
  if y > max_y:
    max_y = y

paper = []
for y in range(max_y+1):
  paper_row = []
  for x in range(max_x+1):
    paper_row.append(' ')
  paper.append(paper_row)

for row in rows:
  x = int(row.split(',')[0])
  y = int(row.split(',')[1])

  paper[y][x] = '#'

empty_row = []
for i in range(len(paper[0])):
  empty_row.append(' ')

if len(paper) % 2 != 0:
  paper.append(empty_row)

for fold in folds:
  if 'y' in fold:
    to_fold = []
    y = int(fold.split('=')[1])

    if len(paper) % 2 == 0:
      for i in range(int(len(paper)/2),len(paper)):
        to_fold.append(paper[i])
      empty_row = []
      if len(to_fold) == len(paper)/2:
        for i in range(len(paper[0])):
          empty_row.append(' ')
        to_fold.append(empty_row)
      to_fold = to_fold[::-1]

      for i_2 in range(len(to_fold)):
        for i_3 in range(len(to_fold[0])):
          if to_fold[i_2][i_3] == '#':
            paper[i_2][i_3] = '#'

      for i in range(int(len(paper)/2),len(paper)):
        paper.pop()

    else:
      for i in range(int(math.floor(len(paper)/2)),len(paper)):
        to_fold.append(paper[i])
      to_fold = to_fold[::-1]

      for i_2 in range(len(to_fold)):
        for i_3 in range(len(to_fold[0])):
          if to_fold[i_2][i_3] == '#':
            paper[i_2][i_3] = '#'
      
      for i in range(int(len(paper)/2),len(paper)):
        paper.pop()

  elif 'x' in fold:
    to_fold = []
    x = int(fold.split('=')[1])
    if len(paper[0]) % 2 == 0:
      for row in paper:
        to_fold_row = []
        for i in range(int(len(paper)/2),len(paper[0])):
          to_fold_row.append(row[i])
        to_fold.append(to_fold_row)
      for row in paper:
        for i in range(int(len(paper)/2),len(paper[0])):
          row.pop()
      for i in range(len(to_fold)):
          to_fold[i] = to_fold[i][::-1]

      for i_2 in range(len(to_fold)):
        for i_3 in range(len(to_fold[0])):
          if to_fold[i_2][i_3] == '#':
            paper[i_2][i_3] = '#'
            
    else:
      for row in paper:
        to_fold_row = []
        for i in range(int(math.ceil(len(paper[0])/2)),len(paper[0])):
          to_fold_row.append(row[i])
        to_fold.append(to_fold_row)
      for i in range(len(to_fold)):
          to_fold[i] = to_fold[i][::-1]

      for i_2 in range(len(to_fold)):
        for i_3 in range(len(to_fold[0])):
          if to_fold[i_2][i_3] == '#':
            paper[i_2][i_3] = '#'

      for row in paper:
        for i in range(int(math.floor(len(row)/2)),len(row)):
          row.pop()

for row in paper:
  print(''.join(row))
