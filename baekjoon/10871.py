import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

for num in numbers:
    if num < X:
        print(num, end=' ')