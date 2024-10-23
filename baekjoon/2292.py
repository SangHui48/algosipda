# n = int(input())
# num = 1
# for i in range(n):
#     num += (i * 6)
#
#     if n <= num:
#         print(i + 1)
#         break

room = int(input())
n = 1
answer = 1
while n < room:
    n = n + answer * 6
    answer += 1

print(answer)