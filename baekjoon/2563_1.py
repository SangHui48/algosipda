import sys

m_input = sys.stdin.readline
n = int(m_input())
points = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, m_input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if points[i][j] == 0:
                points[i][j] = 1

ans = 0

for k in range(1,101):
    for l in range(1, 101):
        if points[k][l] == 1:
            ans += 1

print(ans)