import sys
import heapq

N = int(sys.stdin.readline())
L, R = [], []
for _ in range(N):
  x = int(sys.stdin.readline())
  if len(L) == len(R):
    heapq.heappush(L, -x)
  else:
    heapq.heappush(R, x)

  if R and R[0] < -L[0]:
    left = heapq.heappop(L)
    right = heapq.heappop(R)

    heapq.heappush(L, -right)
    heapq.heappush(R, -left)
  print(-L[0])