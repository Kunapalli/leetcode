# https://leetcode.com/problems/perfect-squares/
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
def numSquares(n):
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    sqlist = []
    for i in range(1, n+1):
        if i <= int(n**0.5):
            sqlist.append(i*i)
            i += 1
        else:
            break
        
    m = len(sqlist)
    for v in range(1, n+1):
        for j in sqlist:
            if v >= j:
                dp[v] = min(dp[v], 1 + dp[v - j]) # either v doesn't include j or v includes at least one j
            else:
                break
       
    print(dp)
    return dp[n]

print(numSquares(117))
