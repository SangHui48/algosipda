dial = {
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
}

s = input()
ans = 0
for x in s:
    for k, v in dial.items():
        if x in v:
            ans += ((k-1) + 2)
print(ans)