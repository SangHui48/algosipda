import sys

m_input = sys.stdin.readline

n, m, k = map(int, m_input().split())
data = list(map(int, m_input().split()))

data.sort(reverse=True)
ans = ((data[0] * k) + data[1]) * (m // (k + 1)) + (data[0] * (m % (k + 1)))
print(ans)