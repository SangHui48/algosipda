import sys

m_input = sys.stdin.readline

n, m = map(int, m_input().split())
card = [list(map(int, m_input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    ans = max(ans, min(card[i]))

print(ans)