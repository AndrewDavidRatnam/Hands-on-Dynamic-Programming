# n = int(input()) 
# l1 = [int(i) for i in input().strip().split()] 
# l2 = [int(i) for i in input().strip().split()] 
l1 = [8,6,2,3]
l2 = [9,7,1,2]
def display(l1, l2):
    # print(l1)
    # print(l2)
    new_list = [l1,l2]
    for list in new_list:
        print(list)
    n = len(l1)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = abs(new_list[0][0] - new_list[1][0])
    for i in range(2,n+1):
        vert, horz = max_possible(new_list,i,n)
        print(vert, horz)
        vert = vert + dp[i-1]
        dp[i] = max(vert,horz)
    print(dp[-1])
def max_possible(new_list,index,n):
    i , j = 0,index
    print(f"At Column:",j)
    max_abs_diff_vert = 0
    max_abs_diff_horz = 0
    # if j == 0 :
    #     max_abs_diff_vert = abs(new_list[i][j-1] - abs(new_list[i+1][j-1]))  
    #     max_abs_diff_horz =abs(new_list[i][j-1] - abs(new_list[i][j]))  
    # if j >= 0 and j < n-1:
    max_abs_diff_vert = abs(new_list[i][j-1] - abs(new_list[i+1][j-1])) #,abs(new_list[i][j] - abs(new_list[i-1][j])) ) 
    max_abs_diff_horz =min(abs(new_list[i][j-1] - abs(new_list[i][j])) ,abs(new_list[i][j] - abs(new_list[i][j+1])) ) 
    # if j == n-1:
    #     max_abs_diff_vert = abs(new_list[i][j-1] - abs(new_list[i-1][j-1]))  
    #     max_abs_diff_horz =abs(new_list[i][j] - abs(new_list[i][j-2]))  
    # print("----------------------")
    return (max_abs_diff_vert,max_abs_diff_horz )
def solve(l1,l2):
    grid = [l1,l2]
    N = len(l1)
    dp = [0] * (N + 1)
    dp[0] = 0  # Base case: no columns
    dp[1] = abs(grid[0][0] - grid[1][0])  # Base case: 1 column, vertical tile
    
    # Fill DP table
    for i in range(2, N + 1):
        # Option 1: Vertical tile at column i
        vertical_score = abs(grid[0][i-1] - grid[1][i-1])
        dp[i] = dp[i-1] + vertical_score
        
        # Option 2: Two horizontal tiles covering columns (i-1) and i
        horizontal_score = abs(grid[0][i-2] - grid[0][i-1]) + abs(grid[1][i-2] - grid[1][i-1])
        dp[i] = max(dp[i], dp[i-2] + horizontal_score)
    
    return dp[N]


print(solve(l1,l2))