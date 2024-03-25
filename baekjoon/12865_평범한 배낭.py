import sys

m_input = sys.stdin.readline

N, K = map(int, m_input().split())
pack = [[0, 0]]
dp = [[0] * ( K + 1) for _ in range(N + 1)]

for _ in range(N):
    pack.append(list(map(int, m_input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        W = pack[i][0]
        V = pack[i][1]

        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-W] + V, dp[i-1][j])

print(dp[-1][-1])