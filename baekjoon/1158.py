N, K = map(int, input().split())

x = [i for i in range(1, N + 1)]
ans = []
idx = 0
while x:
    idx = (idx + K - 1) % len(x)
    ans.append(x.pop(idx))

print("<" + ", ".join(map(str, ans)) + ">")