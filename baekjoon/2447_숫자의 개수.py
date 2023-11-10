cnt = [0] * 10

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

for num in result:
    cnt[int(num)] += 1

for x in cnt:
    print(x)