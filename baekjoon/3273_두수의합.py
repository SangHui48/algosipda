import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

left, right = 0, n-1
answer = 0

while left < right:
    result = nums[left] + nums[right]
    if result < x:
        left += 1
    elif result > x:
        right -= 1
    else:
        left += 1
        right -= 1
        answer += 1
print(answer)