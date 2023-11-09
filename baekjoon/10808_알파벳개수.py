dict = [0] * 26

S = input()

for s in S:
    dict[ord(s) - 97] += 1

print(' '.join(map(str, dict)))