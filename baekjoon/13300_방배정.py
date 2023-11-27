N, K = map(int, input().split())

man = [0] * 7
woman = [0] * 7
answer = 0

for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        woman[Y] += 1
    else:
        man[Y] += 1

for i in range(1, 7):
    if man[i] > 0:
        if man[i] % K == 0:
            answer += (man[i] // K)
        else:
            answer += (man[i] // K) + 1
    if woman[i] > 0:
        if woman[i] % K == 0:
            answer += (woman[i] // K)
        else:
            answer += (woman[i] // K) + 1
    
print(answer)