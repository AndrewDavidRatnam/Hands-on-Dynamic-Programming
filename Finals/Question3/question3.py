def coin_change_ways(coins, amount):
    dp = [0]*(amount+1)
    dp[0] = 1
    for i in range(1, amount+1):
        for coin in coins:
            print(f"At coin: {coin},  dp: {dp}")
            if i >= coin:
                dp[i] +=dp[i-coin]
    return dp[amount]

coins = [2, 3, 4, 7]
amount = 7
coins = [1, 2, 5]
ampunt = 5
print(coin_change_ways(coins, amount))