s = input()

answer = [0] * 26

for i in range(26):
    if chr(i+97) in s:
        answer[i] = s.index(chr(i+97))
    else:
        answer[i] = -1

print(' '.join(map(str, answer)))