import sys

m_input = sys.stdin.readline

n = int(m_input())
arr = list(map(int, m_input().split()))
ans = 0
cnt = 0
arr.sort()
for data in arr:
    cnt += 1
    if cnt >= data:
        ans += 1
        cnt = 0

print(ans)