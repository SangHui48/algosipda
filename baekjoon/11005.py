n, b = map(int, input().split())

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''

while n:
    answer += str(num_list[n % b])
    n //= b

print(answer[::-1])