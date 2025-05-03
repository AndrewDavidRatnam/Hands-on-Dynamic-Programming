## Problem Statement:Minimize Steps to Reduce to 1
Given an integer n, you are allowed to perform the following operations to reduce it to 1:

    1. Subtract 1 from n.
    2. Divide n by 2 if n is divisible by 2.
    3. Divide n by 3 if n is divisible by 3.

The task is to find the minimum number of operations required to reduce n to 1.

**Write a function minOperations(n) that returns the minimum number of operation to reduce n to 1.**

## Example:

### Input:
n = 10
### Output:
3
### Explanation:
Start with 10.
Subtract 1 → 9.
Divide by 3 → 3.
Divide by 3 → 1.
Total operations: 3.