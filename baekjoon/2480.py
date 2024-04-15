from collections import Counter

data = list(map(int, input().split()))
data_count = Counter(data)
x = list(data_count.values()).

if x == 3:
    print(10000 + (x * 1000))
elif x == 2:
    print(1000 + (x * 100))
else:
    print(data.max() * 100)