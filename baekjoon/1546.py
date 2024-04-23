import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

max_arr = max(arr)

arr = list(map(lambda x: (x / max_arr) * 100, arr))

print(sum(arr) / N)