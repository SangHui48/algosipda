import sys

m_input = sys.stdin.readline

while True:
    data = list(map(int, m_input().split()))
    data.sort()
    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        break

    if data[2] >= data[1] + data[0]:
        print("Invalid")
    elif data[0] == data[1] == data[2]:
        print("Equilateral")
    elif data[0] == data[1] or data[1] == data[2] or data[2] == data[0]:
        print("Isosceles")
    else:
        print("Scalene")