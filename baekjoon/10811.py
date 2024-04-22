import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    arr[i:j+1] = arr[j:i-1:-1]

print(' '.join(map(str, arr[1:])))