import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    type_n = int(input())
    coins = map(int, input().split())
    total = int(input())

    dp = [0] * (total+1)
    dp[0] = 1 #0만드는 건 1개좌나

    for coin in coins:
        for money in range(coin, total+1):
            dp[money] += dp[money-coin]
    print(dp[total])