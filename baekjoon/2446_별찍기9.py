n = int(input())

for i in range(n, 0, -1):
    print(' '*(n-i), end='')
    print('*' * (2*i - 1))
    
for j in range(1, n):
    print(' '* (n-1-j), end='')
    print('*' * (2*j + 1))