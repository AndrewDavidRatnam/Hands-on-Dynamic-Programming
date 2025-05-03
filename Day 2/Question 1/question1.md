## Problem Statement: Climbing Stairs

You are climbing a staircase that has 
 stairs, and you can either take 1 or 2 steps at a time to climb on stairs. Write a function climb_stairs(n) to determine how many distinct ways there are to reach the top of the staircase.
Requirements:

## The input 
 $n$ represents the number of stairs.
Each step can either be taken as a single step (1 step) or as a double step (2 steps).
Use Dynamic Programming to solve the problem efficiently.
Constraints:
$1<=n<=10^4$
 
Example:

Input 1: n = 2

Output: 2

Explanation:

Take two 1-steps: (1, 1)
Take one 2-step: (2) Hence, there are 2 distinct ways to climb 2 steps.
 

Input 2: n = 3

Output: 3

Explanation:

Take three 1-steps: (1, 1, 1)
Take one 2-step followed by a 1-step: (2, 1)
Take one 1-step followed by a 2-step: (1, 2) Hence, there are 3 distinct ways to climb 3 steps.