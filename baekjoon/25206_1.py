total = 0
score_total = 0

dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for _ in range(20):
    name, score, grade = input().split()
    if grade != 'P':
        score_total += float(score)
        total += (float(dic[grade]) * float(score))

print(round(total / score_total, 6))
