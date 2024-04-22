import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [ i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    arr[i], arr[j] = arr[j], arr[i]

print(' '.join(map(str, arr[1:])))