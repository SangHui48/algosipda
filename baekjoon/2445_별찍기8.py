n = int(input())

for i in range(n):
    print('*' * (i+1), end='')
    print(' ' * ((2*n) - ((i+1) * 2)), end='')
    print('*' * (i+1))

for j in range(n-1, 0, -1):
    print('*' * j, end='')
    print(' ' * ((2*n) - (2*j)), end='')
    print('*' * j)