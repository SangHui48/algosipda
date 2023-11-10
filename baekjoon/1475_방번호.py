# word = input()

# answer = [0] * 10

# for i in range(len(word)):
#     num = int(word[i])
    
#     if num == 6 or num == 9:
#         if answer[6] <= answer[9]:
#             answer[6] += 1
#         else:
#             answer[9] += 1
#     else:
#         answer[num] += 1
        
# print(max(answer))

f = input().count

print([*map(f, "012345678")] + [(f("6") + f("9") + 1) // 2])