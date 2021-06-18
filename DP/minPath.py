def getMinSumPathDp(arr, n):
    dp = [ [0 for i in range(n+1)] for i in range(n+1) ]
    for i in range(n, 0, -1):
        dp[i-1][n-1] = arr[i-1][n-1] + dp[i][n-1]
    for i in range(n, 0, -1):
        dp[n-1][i-1] = arr[n-1][i-1] + dp[n-1][i]
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = arr[i][j] + min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1])
    print(dp)



arr = [
    [4, 3, 2, 6],
    [1, 8, 9, 8],
    [1, 1, 8, 9],
    [1, 1, 8, 2]
]
print(getMinSumPathDp(arr, len(arr)))