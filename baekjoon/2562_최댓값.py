import sys

input = sys.stdin.readline

max = 1
max_val = 0
for i in range(9):
    data = int(input())
    if data > max_val:
        max_val = data
        max = i + 1

print(max_val, max)