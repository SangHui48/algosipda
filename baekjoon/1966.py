import sys
from collections import deque

m_input = sys.stdin.readline

T = int(m_input())

for _ in range(T):
    N, M = map(int, m_input().split())
    q = deque(list(map(int, m_input().split())))
    printer = [(idx, imp) for idx, imp in enumerate(q)]
    q.sort(reverse=True)


# t = int(m_input())
#
# for _ in range(t):
#     n, m = map(int, m_input().split())
#     q =deque(list(map(int, m_input().split())))
#     ans = 1
#     while q:
#         if q[0] < max(q):
#             q.append(q.popleft())
#         else:
#             if m == 0:
#                 break
#             q.popleft()
#             ans += 1
#
#         if m > 0:
#             m -= 1
#         else:
#             m = len(q) - 1
#     print(ans)