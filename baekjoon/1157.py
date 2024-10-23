# from collections import Counter
#
# s = Counter(input().upper())
# arr = s.most_common(2)
# if len(arr) > 1:
#     if arr[0][1] == arr[1][1]:
#         print('?')
#     else:
#         print(arr[0][0])
# else:
#     print(arr[0][0])

from collections import Counter

s = Counter(input().upper())
arr = s.most_common(2)
if len(arr) > 1:
    if arr[0][1] == arr[1][1]:
        print('?')
    else:
        print(arr[0][0])
else:
    print(arr[0][0])