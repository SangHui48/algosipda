h, m = map(int, input().split())

x = h * 60 + m
y = x - 45

if y < 0:
    print(23, y % 60)
else:
    print(y // 60, y % 60)
