# Minimum Moves to End

You are given a list steps with n positive integers. You are at index 0 initially, and you can make multiple moves, in each move, you can jump up to a certain number of positions forward, as determined by the value at their current position. For instance, if the number at the current index i is 3, it indicates that you can jump from index i to either index i+1 or i+2, or i+3 with just one move. The goal is to reach the end of the list (at index n-1) with the minimum number of moves.

**Write a function min_moves_to_end(steps) that takes a list steps of positive integers and returns the minimum number of moves required to reach the end of the list.**

**Sample Input 1**
[2, 3, 1, 1, 2] #steps

**Output:**
2 #minimum number of moves

## Explanation

First move: Index 0 to index 1

Second Move: Index 1 to last index 4

 
**Sample Input 2**
[1, 1, 1, 1, 1]

**Output:**
4

## Explanation

First move: Index 0 to index 1

Second Move: Index 1 to index 2

Third Move: Index 2 to index 3

Fourth Move: Index 3 to index 4