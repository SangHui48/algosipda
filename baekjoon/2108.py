import sys
from collections import Counter

m_input = sys.stdin.readline

n = int(m_input())
data = []
for _ in range(n):
    data.append(int(m_input()))

data.sort()
print(round(sum(data) / n))
print(data[n//2])

dic = Counter(data)
mx = max(dic.values())
mx_list = []

for i in dic:
    if mx == dic[i]:
        mx_list.append(i)

if len(mx_list) > 1:
    print(mx_list[1])
else:
    print(mx_list[0])

print(data[-1] - data[0])