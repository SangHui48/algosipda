import sys

m_input = sys.stdin.readline

m = int(m_input())
s = set()
for _ in range(m):
    command = m_input().split()

    if command[0] == "add":
       s.add(int(command[1]))
    elif command[0] == "remove":
        s.discard(int(command[1]))
    elif command[0] == "check":
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if int(command[1]) in s:
            s.discard(int(command[1]))
        else:
            s.add(int(command[1]))
    elif command[0] == "all":
        s = set([i for i in range(1, 21)])
    elif command[0] == "empty":
        s = set()