coins = [500, 100, 50, 10]

n = 1260
ans = 0

for coin in coins:
    ans += n // coin
    n %= coin

print(ans)