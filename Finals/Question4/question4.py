def min_cost(m, n, grid_costs):
    if m == 1 and n == 1:
        return grid_costs[0][0]
    for j in range(1, n):
        grid_costs[0][j] += grid_costs[0][j-1]
    for i in range(1, m):
        grid_costs[i][0] += grid_costs[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid_costs[i][j] += min(grid_costs[i-1][j], grid_costs[i][j-1])
    return grid_costs[m-1][n-1]


m, n = 3, 3
grid_costs = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_cost(m, n, grid_costs))  # Output: 7

grid_costs = [[1, 3, 2], [1, 2, 4], [4, 1, 1]]
print(min_cost(m, n, grid_costs))  # Output: 6

m, n = 4, 3
grid_costs = [[1, 5, 1],[1, 2, 4], [6, 1, 2],[1, 5, 1]]
print(min_cost(m, n, grid_costs)) 
