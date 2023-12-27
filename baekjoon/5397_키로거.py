import sys
get = sys.stdin.readline

L = int(get())
for _ in range(L):
    commands = list(get().rstrip())
    st1 = []
    st2 = []
    for command in commands:
        
        if command == '<':
            if st1:
                st2.append(st1.pop())
        elif command == '>':
            if st2:
                st1.append(st2.pop())
        elif command == '-':
            if st1:
                st1.pop()
        else:
            st1.append(command)
        
    st1.extend(reversed(st2))
    print(''.join(st1)) 
    