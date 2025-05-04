def minCoins(coins, amount):
    min_coin = [float('inf')] * (amount + 1)
    min_coin[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                min_coin[i] = min(min_coin[i], min_coin[i - coin] + 1)
    return min_coin[amount] if min_coin[amount] != float('inf') else -1

coins = [1, 3, 4]
amount = 6
print(minCoins(coins,amount))