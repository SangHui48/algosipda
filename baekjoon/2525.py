A, B = map(int, input().split())
C = int(input())

result = A * 60 + B + C

if result // 60 > 23:
    print((result // 60) - 24, result % 60)
else:
    print(result // 60, result % 60)