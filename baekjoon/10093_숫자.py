a, b = map(int, input().split())
a = min(a, b)
b = max(a, b)
n = a - b - 1
if a == b or n + 1 == b:
    n = 0
print(n)
for i in range(a+1, b):
    print(i, end=" ")