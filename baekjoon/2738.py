import sys

a, b = [], []

n, m = map(int, sys.stdin.readline().rstrip().split())
ans = [[0] * m for _ in range(n)]

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

for _ in range(n):
    b.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(m):
        ans[i][j] = a[i][j] + b[i][j]

for i in range(n):
    for j in range(m):
        print(ans[i][j], end= ' ')
    print()