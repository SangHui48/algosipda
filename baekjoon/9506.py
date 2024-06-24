import sys

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == -1:
        break

    arr = [1]
    for i in range(2, n):
        if n % i == 0:
            arr.append(i)

    if sum(arr) == n:
        ans = f'{n} = ' + ' + '.join(map(str, arr))
        print(ans)
    else:
        print(f'{n} is NOT perfect.')
