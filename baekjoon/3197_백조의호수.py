from collections import deque
import sys

dy, dx = (-1, 0, 1, 0) , (0, -1, 0, 1)

def find_swan(lake, visited, queue):
  next_queue = deque()
  while queue:
    y, x = queue.popleft()
    if y == swan[1][0] and x == swan[1][1]:
      return True, None
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if not 0<=ny<row or not 0<=nx<col:
        continue
      if visited[ny][nx]:
        continue
      if lake[ny][nx] == 'X':
        next_queue.append((ny,nx))
      else:
        queue.append((ny, nx))
      visited[ny][nx] = True

  return False, next_queue

def melt_ice(water, lake):
  next_water = deque()
  while water:
    y, x = water.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if not 0<=ny<row or not 0<=nx<col:
        continue
      if lake[ny][nx] == 'X':
        next_water.append((ny, nx))
        lake[ny][nx] = '.'

  return next_water
      
      

row, col = map(int, sys.stdin.readline().split())
lake = []
swan = []
water = deque() # 물의 좌표를 담은 큐 상하좌우에 X가 있는지 확인해야함

for rr in range(row):
  cur = list(sys.stdin.readline().rstrip())
  for cc, vv in enumerate(cur):
    if vv == '.' or vv == 'L':
      water.append((rr, cc))
    if vv == 'L':
      swan.append((rr, cc))
  lake.append(cur)

day = -1
visited = [[False] * col for _ in range(row)]
queue = deque() # 백조가 다른 백조를 찾을때 사용할 큐

y, x = swan[0][0], swan[0][1]
queue.append((y, x))
visited[y][x] = True

while True:
  day += 1
  found, next_queue = find_swan(lake, visited, queue)
  if found:
    break
  water = melt_ice(water, lake)
  queue = next_queue

print(day)