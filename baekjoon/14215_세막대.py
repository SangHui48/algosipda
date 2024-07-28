x = sorted(list(map(int, input().split())))
if x[0] + x[1] > x[2]:
    print(sum(x))
else:
    print(2*(x[0] + x[1]) - 1)