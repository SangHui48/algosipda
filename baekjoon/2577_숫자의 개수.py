dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,}

data = [int(input()) for _ in range(3)]

total = 1
for i in range(3):
    total *= data[i]

total = str(total)
for num in total:
    dict[num] += 1

for v in dict.values():
    print(v)
