def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m == 0 and n == 0:
        return 0
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[-1][-1]


for i in range(11):
    print(uniquePaths(i,i))
    i += 1
