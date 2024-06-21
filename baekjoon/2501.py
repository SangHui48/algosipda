n, k = map(int, input().split())
rank = 0
for i in range(1, n+1):
    if n % i == 0:
        rank += 1
        if rank == k:
            print(i)
            break

if rank < k:
    print(0)