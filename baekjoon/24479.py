import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

c = 1
def dfs(graph, v, visited):
  global c
  visited[v] = c

  for i in graph[v]:
    if visited[i] == 0:
      c += 1
      dfs(graph, i, visited)

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N+1):
  graph[i].sort()

dfs(graph, R, visited)

for i in range(1, N+1):
  print(visited[i])