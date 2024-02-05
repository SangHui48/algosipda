import sys
m_input = sys.stdin.readline

stack = []

N = int(m_input())

for _ in range(N):
    commands = m_input().split()
    if commands[0] == 'push':
        stack.append(int(commands[1]))
    elif commands[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(stack))
    elif commands[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif commands[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)