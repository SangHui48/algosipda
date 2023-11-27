cnt = [0] * 26

a = list(input())
b = list(input())
for i in a:
    cnt[ord(i)- 97] += 1
for j in b:
    cnt[ord(j) - 97] -= 1

print(sum(map(abs, cnt)))