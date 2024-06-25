import math

m = int(input())
n = int(input())

arr = []

for i in range(m, n+1):
    if i > 1:
        flag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
            
        if flag:
            arr.append(i)
        
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])