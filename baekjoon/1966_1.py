from collections import deque
import sys

m_input = sys.stdin.readline

t = int(m_input())
for _ in range(t):
    n, m = map(int, m_input().split())
    q = deque(list(map(int, m_input().split())))
    cnt = 0

    while q:
        best = max(q)
        now = q.popleft()
        m -= 1

        if now == best:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            q.append(now)
            if m < 0:
                m = len(q) - 1