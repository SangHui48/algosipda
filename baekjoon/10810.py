import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for idx in range(i, j+1):
        arr[idx] = k

for x in arr[1:]:
    print(x, end=' ')