import sys

m_input = sys.stdin.readline
n = int(m_input())
chn = []
for _ in range(n):
    chn.append(m_input().rstrip())

ans = []
cur = 0

while chn[cur] != 'KBS1':
    cur += 1
    ans.append(1)

for _ in range(cur):
    ans.append(4)

cur = 0
chn.remove('KBS1')
chn = ['KBS1'] + chn
while chn[cur] != 'KBS2':
    cur += 1
    ans.append(1)

for _ in range(cur - 1):
    ans.append(4)

print(''.join(map(str, ans)))