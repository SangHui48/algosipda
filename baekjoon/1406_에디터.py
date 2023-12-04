import sys
input = sys.stdin.readline

st1 = list(input())
st2 = []

M = int(input())

for _ in range(M):
    commands = list(input().split())
    
    if commands[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif commands[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif commands[0] == 'B':
        if st1:
            st1.pop()
    elif commands[0] == 'P':
        st1.append(commands[1])
        
st1.extend()
