n = int(input())

for i in range(n):
    print(' ' * (n-i-1), end='')
    print('*' * (2*i+1))

for j in range(n-1, 0, -1):
    print(' '*(n-j), end='')
    print('*' * (2*j -1))