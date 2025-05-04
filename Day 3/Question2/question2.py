def maxProfit(cost,profit,B):
    n = len(cost)
    dp = [0]*(B+1)

    for i in range(n):
        for b in range(B,cost[i]-1,-1):
            dp[b] = max(dp[b], dp[b - cost[i]] + profit[i])
    return dp[-1]
# cost = [1, 3, 4, 5]
# profit = [10, 40, 50, 70]
# B = 8
# cost = [2, 2, 3, 4]
# profit =[20, 30, 50, 60]
# B =5

cost = [1, 2, 3, 8]
profit =[10, 20, 30, 100]
B =10
print(maxProfit(cost, profit, B)) 