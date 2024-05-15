import sys

T = int(sys.stdin.readline().rstrip())
coins = [25, 10, 5, 1]

for _ in range(T):
    answer = [0, 0, 0, 0]
    c = int(sys.stdin.readline().rstrip())

    for i, coin in enumerate(coins):
        answer[i] += c // coin
        c %= coin

    print(*answer)
