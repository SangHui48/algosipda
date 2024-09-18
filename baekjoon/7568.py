N = int(input())
persons = []
ans = [0] * N
for _ in range(N):
    a, b = map(int, input().split())
    persons.append((a, b))

for i in range(N):
    cnt = 0
    for j in range(N):
        if persons[j][0] > persons[i][0] and persons[j][1] > persons[i][1]:
            cnt += 1
    ans[i] = cnt + 1

print(" ".join(map(str, ans)))