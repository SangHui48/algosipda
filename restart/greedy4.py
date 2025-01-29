import sys

m_input = sys.stdin.readline

n, k = map(int, m_input().split())
ans = 0

# while n > 1:
#     if n % k == 0:
#         n //= k
#         ans += 1
#     else:
#         n -= 1
#         ans += 1

while True:
    target = n - (n % k)
    ans += n - target
    n = target
    if n < k:
        break
    n //= k
    ans += 1

ans += (n - 1)
print(ans)