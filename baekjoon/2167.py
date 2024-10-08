import sys

m_input = sys.stdin.readline

n, m = map(int, m_input().split())
arr = [list(map(int, m_input().split())) for _ in range(n)]

k = int(m_input())
dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(k):
    i, j, x, y = map(int, m_input().split())
    print(dp[x][y] - (dp[i-1][y] + dp[x][j-1]) + dp[i-1][j-1])