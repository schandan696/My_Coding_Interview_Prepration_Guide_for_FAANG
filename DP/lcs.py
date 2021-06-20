def lcs(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1
    dp = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    print(dp)
    return dp[n-1][m-1]


s1 = "abcadc"
s2 = "cadc"
print(lcs(s1, s2))