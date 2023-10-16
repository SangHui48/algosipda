n = int(input())
times = list(map(int, input().split()))

y = m = 0
for time in times:
    y += (time // 30 + 1) * 10
    m += (time // 60 + 1) * 15

if y < m:
    print('Y', y)
elif y == m:
    print('Y', 'M', y)
else:
    print('M', m)