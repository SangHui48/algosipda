arr = [1, 1, 2, 2, 2, 8]

d = list(map(int, input().split()))
for i in range(len(d)):
    print(arr[i] - d[i], end=' ')