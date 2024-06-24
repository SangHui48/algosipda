import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for x in arr:
    if x == 1:
        continue

    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                ans += 1
            break

print(ans)