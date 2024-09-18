check = [0] * 10001

for i in range(1, 10001):
    d = i
    temp = i

    while temp > 0:
        d += temp % 10
        temp = temp // 10

    if d <= 10000:
        check[d] = 1

for i in range(1, 10001):
    if check[i] == 0:
        print(i)
