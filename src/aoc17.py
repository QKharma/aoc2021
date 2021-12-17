input_file = open('./inputs/aoc17.txt', 'r')
target = input_file.read()

target = target.split(': ')[1]

target_x = target.split(', ')[0][2:]
target_x = [int(target_x.split('..')[0]),int(target_x.split('..')[1])]

target_y = target.split(', ')[1][2:]
target_y = [int(target_y.split('..')[0]),int(target_y.split('..')[1])]

def step(x, y, x_vel, y_vel):

  x += x_vel
  y += y_vel
  if x_vel > 0:
    x_vel -= 1
  elif x_vel < 0:
    x_vel += 1
  else:
    x_vel = 0

  y_vel -= 1

  return x,y,x_vel,y_vel

min_x_vel = 0
for i in range(100):
  if i*(i+1)/2 > target_x[0]:
    min_x_vel = i-1
    break

min_y_vel = target_y[0]
max_y_vel = abs(target_y[0])
max_x_vel = target_x[1]

highest_y_vel = 0
hit_vel = set()

for i_y_vel in range(min_y_vel,max_y_vel):
  for i_x_vel in range(min_x_vel,max_x_vel+1):
    x = y = 0
    x_vel = i_x_vel
    y_vel = i_y_vel
    for _ in range(300):
      x, y, x_vel, y_vel = step(x, y, x_vel, y_vel)
      if x >= target_x[0] and x <= target_x[1] and y >= target_y[0] and y <= target_y[1]:
        hit_vel.add((i_x_vel,i_y_vel))
        if i_y_vel > highest_y_vel:
          highest_y_vel = i_y_vel

highest_y = int(highest_y_vel*(highest_y_vel+1)/2)

print(highest_y)
print(len(hit_vel))
