import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    r, s = sys.stdin.readline().rstrip().split()
    r = int(r)

    answer = ''
    for x in s:
        answer += (x * r)
    print(answer)