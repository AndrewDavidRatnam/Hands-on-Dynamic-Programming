def longest_decreasing_subsquence(L):
    n = len(L)
    if n==0:
        return 0
    
    dp = [1]*n

    for i in range(n):
        for j in range(i):
            if L[j] > L[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


L = [[20,15,8,12,2],[5,10,3],[1,6,18,4,5]]   
print(f"{[longest_decreasing_subsquence(_) for _ in L]}")