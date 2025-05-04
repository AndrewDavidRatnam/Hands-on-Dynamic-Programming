def longestPalindromicSubsequence(s):
    n = len(s)
    if n==0:
        return 0
    
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1 
    for sublength in range(2,n+1):
        print(sublength)
        print(f"Value : {sublength}, String:",s[:sublength])
        print(f"Value : {n-sublength + 1}, String:",s[:n-sublength + 1])
        for i in range(n-sublength + 1):
            j = i + sublength - 1

            if sublength == 2:
                if s[i] == s[j]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 1
            else:
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]


# s = ["bbabcbcab","abcd","baaac"]
# print([longestPalindromicSubsequence(a) for a in s])

print("ANS:",longestPalindromicSubsequence("bbabcbcab"))