from collections import Counter

data = list(map(int, input().split()))
data_count = Counter(data)
answer = 0
max_val = 0
for k, v in data_count.most_common():
    if v == 3:
        answer = 10000 + (k * 1000)
        break
    elif v == 2:
        answer = 1000 + (k * 100)
        break
    else:
        if k > max_val:
            max_val = k
            
if max_val:
    answer = (max_val) * 100
    
print(answer)