import sys

a = [ list(sys.stdin.readline().rstrip()) for _ in range(5) ]

for j in range(15):
    for i in range(5):
        if j < len(a[i]):
            print(a[i][j], end='')