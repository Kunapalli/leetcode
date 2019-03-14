def combinationSum(nums, S):
    """
    :type rods: List[int]
    :rtype: int
    """
    n = max(max(nums), S)
    dp = [dict() for i in range(n+1)]
    for i in nums:
        dp[i][(1,)] = (i,)

    for i in range(len(nums)):
        for j in range(nums[i], S+1, 1):
            f1 = dp[nums[i]]
            f2 = dp[j - nums[i]]
            for r in f1:
                for s in f2:
                    x = list(dp[nums[i]][r] + dp[j-nums[i]][s])
                    x.sort()
                    dp[j][tuple(x)] = tuple(x)

    return [list(v) for k,v in dp[S].items()]


print(combinationSum([3,5,7],20))

