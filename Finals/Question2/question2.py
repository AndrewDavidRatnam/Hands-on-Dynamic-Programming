def min_moves_to_end(steps):
    n = len(steps)
    if n <= 0:
        return 0
    if n == 1:
        return steps[0]
    dp = [n+2]*n
    dp[0] = 0
    for i in range(1,steps[0]):
        dp[i] = 1
    
    for i in range(0,n):
        print (f"At step {i}:{dp}")
        print(f"Available steps {steps[i]}")
        for j in range(1,steps[i]+1):
            print (f"At step {i} with jump{j}:{dp}")
            if i+j <= n-1:
                print (f"At step {i} with jump{j}:{dp} \n dp[{i}+{j}]:{dp[i+j]}, dp[{i}]:{dp[i]}, dp[{j}]:{dp[j]}")
                dp[i+j] = min(dp[i+j], dp[i]+1)
                print(f"MIN: of dp[{i+j}]: {min(dp[i+j], dp[i] +1)}")
        
    return dp[-1]
steps = [2, 3, 1, 1, 2]
#steps = [1, 1, 1, 1, 1]
#steps = [2, 3, 1, 1, 2, 4, 2, 1, 1, 1]
print(min_moves_to_end(steps))