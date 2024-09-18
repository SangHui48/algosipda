import sys

m_input = sys.stdin.readline
K = int(m_input())
stack = []

for _ in range(K):
    num = int(m_input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))