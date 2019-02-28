# leetcode https://leetcode.com/problems/coin-change/ has a similar problem. There we are asked to compute fewest number of
# coins to make a certain denomination
# in the below problem, we are looking for total number of distinct ways to make a certain denomination
#
# This is a classic DP algorithm.
# what does dp[i][j] contain? first index i is for amount of change that can be made with
# using first j types of coins. This is the key!
# take example coins [1,2,3], amount = 6
# so dp[6][2] = number of ways to make amount 6 with possible use of first three coins. Note we don't need to use all
# three in a given arrangement. We need to make sure all arrangements that could possibly include one or
# more of these three coins are covered. 
# which means
# dp[6][1] = number of ways to make amount 6 with first two coins. Why does it go like this?
# it seems like we are excluding or including from the last and not sure if this will be correct
# In order to understand this better, let us write like this:
# notation: a,[b,c,d] = amount 'a' with list of coins [b,c,d]

# 6,[1,2,3] = 3,[1,2,3] + 6,[1,2]
# Above we are saying that number of ways to make 6 that include 3 = number of ways to
# make 3 with at least one 3 + number of ways to make 6 from [1,2]
# 
# Again, why are we subtracting '3'. Is that special? No.
# In general, we can prove:
# 6,[1,2,3] = 3,[1,2,3] + 6,[1,2] = 3 + 4 {this is for with or without 3]
# 6,[1,2,3] = 4,[1,2,3] + 6,[2,3] = 4 + 3 {this is for with or without 2]
# 6,[1,2,3] = 5,[1,2,3] + 6,[1,3] = 5 + 2 {this is for with or without 1]
# It makes sense that no matter how we proceed, the final answer is correct.
# one more thing. 3,[1,2,3] could have included ways that excluded 3. So when we say we
# included a number, it is only for that iteration. Later iterations could include or exclude it. 
#
# We can also use venn diagrams to better understand this.
# Let A represent 1, B represent 2 and C represent 3 and let amount = 6
'''
                     B--------------------------------B
 A-------------------|---------------A                |
 | (1,1,1,1,1,1)     |(1,1,1,1,2,2)  |     (2,2,2)    |
 |                   |(1,1,2,2)      |                |
 |                   |               |                |
 |    C--------------|---------------|----------------|------------C
 |    | (1,1,1,3,3)  |  (1,2,3)      |                |            |
 |    |              |               |        ()      |            |
 A----|---- ---------|---------------A                |            |
      |              B--------------------------------B            |
      |                                                            |                      
      |                              (3,3)                         |
      C------------------------------------------------------------C

Consider 6,[1,2,3] = 3,[1,2,3] + 6,[1,2]
From the venn diagram, we can see that 
6,[1,2] = 6,[1,2,3] - C
6,[2,3] = 6,[1,2,3] - A
6,[1,3] = 6,[1,2,3] - B
Furthermore, it is obvious that C = 3,[1,2,3]. 
Number of ways to make 6,[1,2,3] with atleast one 3 is is the same as the number of ways to make 3,[1,2,3]. 
Number of ways to make 6,[1,2,3] with atleast one 1 is is the same as the number of ways to make 5,[1,2,3].
Number of ways to make 6,[1,2,3] with atleast one 2 is is the same as the number of ways to make 4,[1,2,3].
Hence, C = 3,[1,2,3], B=4,[1,2,3], A = 5,[1,2,3]

and this explains that the order of coins in the coin list does not matter. 

Principle of inclusion-exclusion. 
A = 5
B = 4
C = 3
A inter B = 3
B inter C = 1
C inter A = 2
A inter B inter C = 1

From the principle of inclusion, exclusion, we have:
A union B union C = A + B + C - (A inter B) - (B inter C) - (C inter A) + (A inter B inter C)
                  = 5 + 4 + 3 - 3 - 1 - 2 + 1 
                  = 7
'''        

def coinChangeNumOfWays(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    m = len(coins)
    dp = [[0 for x in range(m)] for x in range(amount + 1)]

    for i in range(m):
        dp[0][i] = 1
        
    for i in range(1, amount + 1):
        for j in range(m):
            print(i,j)
            x = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0
            y = dp[i][j - 1] if j >=1 else 0
            dp[i][j] = x + y

    print(dp)
    return dp[amount][m-1]


print(coinChangeNumOfWays([1, 3, 2], 6))
