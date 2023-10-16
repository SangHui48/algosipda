card = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    card = card[:a-1] + card[a-1:b][::-1] + card[b:]

print(' '.join(map(str,card)))