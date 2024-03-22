import sys
m_input = sys.stdin.readline

N, M = map(int, m_input().split())
numbers = list(map(int, m_input().split()))

prefix_sum = [0]
temp = 0

for num in numbers:
    temp += num
    prefix_sum.append(temp)
    
for _ in range(M):
    start, end = map(int, m_input().split())
    print(prefix_sum)
    print(prefix_sum[end] - prefix_sum[start-1])