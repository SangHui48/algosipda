import sys

m_input = sys.stdin.readline

N = int(m_input())
numbers = list(map(int, m_input().split()))
result = 0

for k in range(N):
    find = numbers[k]
    i = 0
    j = N-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    
    while i < j:
        if numbers[i] + numbers[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif numbers[i] + numbers[j] < find:
            i += 1
        else:
            j -= 1
            
print(result)