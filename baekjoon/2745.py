num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
b = int(b)
answer = 0
for i, num in enumerate(n[::-1]):
    answer += b ** i * num_list.index(num)

print(answer)