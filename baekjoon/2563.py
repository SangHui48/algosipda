import sys

arr = [[0] * 100 for _ in range(100)]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(b-1, b+9):
        for j in range(a-1, a+9):
            arr[i][j] = 1

result = 0
for i in range(100):
    result += arr[i].count(1)
print(result)