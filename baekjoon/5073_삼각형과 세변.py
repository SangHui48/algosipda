while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    longest = max(a, b, c)
    if a + b + c - longest > longest:
        if a == b and b == c:
            print('Equilateral')
        elif a == b or b == c or c == a:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')