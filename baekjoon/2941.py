s = input()

voc = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in voc:
    s = s.replace(x, '*')

print(len(s))