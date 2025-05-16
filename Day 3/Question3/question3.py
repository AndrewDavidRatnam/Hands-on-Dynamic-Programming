def uniquePathCount(grid):
    if not grid or not grid[0]:
        return 0
    
    m = len(grid) # rows
    n = len(grid[0])

    if grid[0][0] == 1:
        return 0

    dp = [[0]*n for _ in range(m)]

    dp[0][0] = 1
    for j in range(1,n):
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j-1] 

    for i in range(1, m):
        if grid[i][0] == 0:
            dp[i][0] = dp[i-1][0]

    for i in range(1,m):
        for j in range(1,n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]
grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid = [[0, 1, 0], [1, 1, 0], [0, 0, 0]]
print(uniquePathCount(grid))