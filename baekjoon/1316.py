import sys

n = int(input())
ans = n
for _ in range(n):
    s = sys.stdin.readline().rstrip()

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            continue
        elif s[i] in s[i+1:]:
            ans -= 1
            break

print(ans)
