N, K = map(int, input().split())

data = [i for i in range(1, N+1)]
idx = 0
ans = []
while data:
    idx = (idx + K - 1) % len(data)
    ans.append(data.pop(idx))

print("<" + ", ".join(map(str, ans)) + ">")