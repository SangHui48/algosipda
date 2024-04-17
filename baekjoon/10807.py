import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())

cnt = Counter(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())
print(cnt[v])