x = set()

for _ in range(10):
    n = int(input())
    
    x.add(n % 42)
    
print(len(x))