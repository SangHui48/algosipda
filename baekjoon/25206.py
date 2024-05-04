score_total = 0
total = 0
dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    name, score, s = input().split()
    score = float(score)

    if s != 'P':
        total += (score * dic[s])
        score_total += score

print('%.6f' %(total/score_total))