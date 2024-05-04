import sys

a = []
ans, row, col = 0, 0, 0

for _ in range(9):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if a[i][j] >= ans:
            ans = a[i][j]
            row = i + 1
            col = j + 1

print(ans)
print(row, col)