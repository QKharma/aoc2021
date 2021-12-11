class Board():

  def __init__(self, board):
    self.board = board
    self.rows = []
    self.columns = []
    self.won = False
    self.calc_rows_and_columns()

  def set_rows(self):
    for row in board:
      self.rows.append(row.split(' '))
 
  def set_columns(self):
    for i in range(0,len(self.rows)):
      self.columns.append([])
    for i in range(0,len(self.rows)):
      for row in self.rows:
        self.columns[i].append(row[i])

  def calc_rows_and_columns(self):
    self.set_rows()
    self.set_columns()

  def check_if_win(self, drawn_numbers):
    for row in self.rows:
      row_win = True
      for number in row:
        if number not in drawn_numbers:
          row_win = False
      
      if row_win is True:
        return True

    for column in self.columns:
      column_win = True
      for number in column:
        if number not in drawn_numbers:
          column_win = False
      
      if column_win is True:
        return True
    
    return False
        

input_file = open('./inputs/aoc4.txt', 'r')
drawn_numbers = input_file.read().split('\n')[0]

input_file = open('./inputs/aoc4.txt', 'r')
boards = input_file.read().split('\n')
boards.pop(0)
boards.pop(0)

formatted_boards = []
board = []
for elem in boards:
  if elem != '':
    elem = ' '.join(elem.strip().split())
    board.append(elem)
  else:
    formatted_boards.append(Board(board))
    board = []

if board != []:
  formatted_boards.append(Board(board))

#######
#part 1
'''
def calculate_winner():

  drawn_numbers_i = []

  for number in drawn_numbers.split(','):
    drawn_numbers_i.append(number)
    for board in formatted_boards:
      if board.check_if_win(drawn_numbers_i) is True:
        return board, drawn_numbers_i[-1], drawn_numbers_i

winning_board, winning_number, drawn_numbers_final = calculate_winner()

sum_board = 0
for row in winning_board.rows:
  for value in row:
    if value not in drawn_numbers_final:
      sum_board += int(value)

#print(sum_board*int(winning_number))
'''

#######
#part 2
def calculate_winners():

  drawn_numbers_i = []
  winning_boards = []

  for number in drawn_numbers.split(','):

    drawn_numbers_i.append(number)
    for board in formatted_boards:
      if board.check_if_win(drawn_numbers_i) is True and board.won is False:
        winning_boards.append([board, drawn_numbers_i[-1]])
        board.won = True

  return winning_boards

winning_boards = calculate_winners()

winning_board = winning_boards[-1][0]
winning_number = winning_boards[-1][1]

sum_board = 0
drawn_numbers_final = []
for number in drawn_numbers.split(','):
  drawn_numbers_final.append(number)
  if winning_board.check_if_win(drawn_numbers_final) is True:
    break

for row in winning_board.rows:
  for value in row:
    if value not in drawn_numbers_final:
      sum_board += int(value)

print(sum_board*int(winning_number))