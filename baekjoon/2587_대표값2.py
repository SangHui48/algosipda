data = [int(input()) for _ in range(5)]
data.sort()
avg = sum(data) // len(data)
med = data[len(data)//2]

print(avg)
print(med)