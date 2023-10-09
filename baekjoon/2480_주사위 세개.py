from collections import Counter
import sys

input = sys.stdin.readline

data = Counter(map(int, input().split())).most_common()

max_val = data[0][0]
flag = False
answer = 0
for k, v in data:
    if v == 3:
        answer += (10000 + (k * 1000))
        print(answer)
        break
    elif v == 2:
        answer += (1000 + (k * 100))
        print(answer)
        break
    else:
        if max_val <= k:
            max_val = k
            flag = True
if flag:
    print(max_val * 100)