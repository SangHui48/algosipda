import sys
c_input = sys.stdin.readline

K = int(c_input())
stack = []
for _ in range(K):
    data = int(c_input())
    if data == 0:
        stack.pop()
    else:
        stack.append(data)
        
print(sum(stack))