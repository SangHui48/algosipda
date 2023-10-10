import sys

input = sys.stdin.readline

# arr = []
# for _ in range(7):
#     data = int(input())
#     if data % 2 == 1:
#         arr.append(data)
arr = [int(input()) for _ in range(7) if int(input()) % 2 != 0]
print(arr)
if len(arr):
    arr.sort()
    print(sum(arr))
    print(arr[0])
else:
    print(-1)