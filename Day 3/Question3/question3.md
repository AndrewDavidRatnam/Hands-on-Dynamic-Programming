# Problem Statement: Number of unique paths in a grid with obstacles

You have given a grid[m][n]. Assume that we are starting from (0,0) and the goal is to reach (m-1,n-1). Each move is restricted to a 1-step right or 1-step bottom only. The obstacle is marked as 1 and the space is marked as 0 in the grid You need to find the number of unique paths to reach the goal (m-1,n-1).

**Write a function uniquePathCount(grid) that return the number of unique paths to reach the goal (m-1,n-1) from (0,0).**

### Example:

*Input*:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
*Output*:
2
*Explanation*:

There are two ways to reach the bottom-right corner

Right -> Right -> Down -> Down: Start from (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
Down -> Down -> Right -> Right: Start from (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2)
